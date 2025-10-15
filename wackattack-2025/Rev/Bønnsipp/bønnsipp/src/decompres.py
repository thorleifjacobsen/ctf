#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wackbzip2_decompress.py

Pure-Python decompressor for the provided "compress" implementation.

Pipeline reversed:
  file -> [read LE u64 size] -> [read freq[256] as LE u32] -> Huffman decode
      -> stream of temp bytes: [ (u32 stop_index) | RLE block | ... ]
      -> RLE decode (blockwise)
      -> inverse MTF
      -> inverse BWT (with stop_index)
      -> original bytes

Assumptions (matching the C compressor you shared):
- Header: 8-byte little-endian unsigned long: total bytes of the temp stream.
- Then: 256 * 4-byte little-endian unsigned ints: frequency table used to build the Huffman tree.
- Huffman bitstream follows; padded at end; stop decoding after producing exactly the header byte count.
- Temp stream structure (repeated):
    [u32 little-endian stop_index] + [RLE for exactly (block_len+1) bytes after MTF]
  All blocks except the last decode to (MAX_BLOCKSIZE+1) bytes post-MTF.
  The last one may be shorter; it ends exactly at end-of-temp.

Usage:
    python3 wackbzip2_decompress.py input.wackbzip2 output.raw [--blocksize 512]

If your compressor was called with a different blocksize, pass the same value here.
"""
import argparse
import io
import struct
import sys
from collections import Counter
import heapq

# -------------------- Bit reader --------------------
class BitReader:
    def __init__(self, f: io.BufferedReader):
        self.f = f
        self.buf = 0
        self.nbits = 0

    def read_bit(self):
        if self.nbits == 0:
            b = self.f.read(1)
            if not b:
                return None
            self.buf = b[0]
            self.nbits = 8
        bit = (self.buf >> 7) & 1
        self.buf = (self.buf << 1) & 0xFF
        self.nbits -= 1
        return bit

# -------------------- Huffman --------------------
class HuffNode:
    __slots__ = ("freq","sym","left","right","minsym")
    def __init__(self, freq, sym=None, left=None, right=None):
        self.freq = freq
        self.sym = sym
        self.left = left
        self.right = right
        # for stable tie-breaking: minimal symbol in subtree
        if sym is not None:
            self.minsym = sym
        else:
            self.minsym = min(left.minsym, right.minsym)

def build_huffman_tree(freqs):
    # freqs: list of 256 ints
    heap = []
    uid = 0
    for s, f in enumerate(freqs):
        if f > 0:
            node = HuffNode(f, sym=s)
            # heap key: (freq, minsym, uid)
            heapq.heappush(heap, (f, s, uid, node))
            uid += 1
    if not heap:
        # empty stream is valid
        return None
    if len(heap) == 1:
        # single-symbol tree
        return heap[0][3]
    while len(heap) > 1:
        f1, m1, u1, n1 = heapq.heappop(heap)
        f2, m2, u2, n2 = heapq.heappop(heap)
        parent = HuffNode(f1 + f2, left=n1, right=n2)
        heapq.heappush(heap, (parent.freq, parent.minsym, uid, parent))
        uid += 1
    return heap[0][3]

def huffman_decode_bytes(bitreader, root, out_len):
    """
    Decode exactly out_len bytes using the given tree. Ignores trailing padding bits.
    """
    if root is None:
        return b""
    out = bytearray()
    # If single-leaf, every code is zero-length; encoder typically emits 0s; just fill.
    if root.sym is not None and root.left is None and root.right is None:
        out.extend([root.sym] * out_len)
        return bytes(out)

    node = root
    while len(out) < out_len:
        bit = bitreader.read_bit()
        if bit is None:
            raise ValueError("Unexpected end of bitstream while Huffman decoding")
        node = node.left if bit == 0 else node.right
        if node.sym is not None:
            out.append(node.sym)
            node = root
    return bytes(out)

# -------------------- RLE decode (blockwise) --------------------
def rle_decode_block(enc: bytes, start: int, max_symbols: int | None, end_limit: int) -> tuple[bytes, int]:
    """
    Decode one RLE block from enc[start:...]; stop when:
      - we produced exactly max_symbols (if not None), OR
      - we reached end_limit (EOF of temp stream) -> last block.
    Returns (decoded_bytes, bytes_consumed_from_enc).
    """
    out = bytearray()
    i = start
    while i < end_limit:
        # If non-last blocks, we can stop early as soon as we reached target length
        if max_symbols is not None and len(out) == max_symbols:
            break

        count_byte = enc[i]
        i += 1
        signed = count_byte if count_byte < 128 else count_byte - 256

        if signed > 0:
            if i >= end_limit:
                raise ValueError("RLE decode: missing value for repeat run")
            val = enc[i]
            i += 1
            # emit 'signed' copies
            out.extend([val] * signed)
        elif signed < 0:
            n = -signed
            if i + n > end_limit:
                raise ValueError("RLE decode: non-repeat run exceeds input")
            out.extend(enc[i:i+n])
            i += n
        else:
            # zero shouldn't appear in this scheme
            raise ValueError("RLE decode: zero run-length encountered")

    # For non-last blocks, we expect exact match to max_symbols
    if max_symbols is not None and len(out) != max_symbols:
        raise ValueError(f"RLE decode: block produced {len(out)} symbols, expected {max_symbols}")
    return (bytes(out), i - start)

# -------------------- inverse Move-to-Front --------------------
def inverse_mtf(buf: bytearray | bytes) -> bytes:
    mtf = list(range(256))
    out = bytearray()
    for idx in buf:
        c = mtf[idx]
        out.append(c)
        # move to front
        del mtf[idx]
        mtf.insert(0, c)
    return bytes(out)

# -------------------- inverse Burrows–Wheeler --------------------
def inverse_bwt(last_col: bytes, stop_index: int) -> bytes:
    """
    Given 'last_col' of length L (includes sentinel encoded as 0xFF) and stop_index,
    reconstruct the original block of length L-1 (without sentinel).
    LF-mapping with stable ranks per byte.
    """
    L = len(last_col)
    # Tally
    counts = [0]*256
    for b in last_col:
        counts[b] += 1
    # starting positions in first column
    starts = [0]*256
    total = 0
    for b in range(256):
        starts[b] = total
        total += counts[b]
    # ranks and next array
    occ = [0]*256
    next_idx = [0]*L
    for i, b in enumerate(last_col):
        next_idx[starts[b] + occ[b]] = i
        occ[b] += 1
    # walk
    res = bytearray(L-1)
    j = stop_index
    for k in range(L-2, -1, -1):
        j = next_idx[j]
        res[k] = last_col[j]
    return bytes(res)

# -------------------- Main decompressor --------------------
def decompress_wackbzip2(fin: io.BufferedReader, fout: io.BufferedWriter, max_blocksize: int):
    # 1) Header: total temp size (little-endian u64)
    hdr = fin.read(8)
    if len(hdr) != 8:
        raise ValueError("File too short (missing 8-byte size header)")
    (temp_total_len,) = struct.unpack("<Q", hdr)

    # 2) Frequency table: 256 x u32 (little-endian)
    freq_bytes = fin.read(256*4)
    if len(freq_bytes) != 256*4:
        raise ValueError("File too short (missing frequency table)")
    freqs = list(struct.unpack("<256I", freq_bytes))
    if sum(freqs) != temp_total_len:
        raise ValueError("Frequency table sum does not match header size; not a compatible file")

    # 3) Huffman decode temp stream
    tree = build_huffman_tree(freqs)
    br = BitReader(fin)
    temp_stream = huffman_decode_bytes(br, tree, temp_total_len)

    # 4) Parse temp stream into blocks, RLE-decode, inverse MTF, inverse BWT
    off = 0
    temp_len = len(temp_stream)
    out = bytearray()

    while off < temp_len:
        if off + 4 > temp_len:
            raise ValueError("Truncated temp stream before stop_index")
        stop_index = struct.unpack("<I", temp_stream[off:off+4])[0]
        off += 4

        # For all but the last block, decode exactly (MAX_BLOCKSIZE+1) MTF symbols.
        last_block = False
        # We don't know it's last until we try; but RLE runs are self-delimiting.
        # Decode with target MAX_BLOCKSIZE+1 unless we hit EOF of temp stream.
        target = max_blocksize + 1

        # Perform a bounded RLE decode view over temp_stream
        mtf_block, consumed = rle_decode_block(temp_stream, off, target, temp_len)
        off += consumed

        # If we consumed to end of temp AND decoded fewer than target symbols, that's the last block.
        if off >= temp_len and len(mtf_block) < target:
            last_block = True

        # If it's not last and the encoder produced exactly target symbols, proceed.
        # If it *is* last, length may be <= target.
        # Safety check: stop_index must be < len(mtf_block)
        if stop_index >= len(mtf_block):
            raise ValueError(f"stop_index {stop_index} out of range for block of length {len(mtf_block)}")

        # inverse MTF
        last_col = inverse_mtf(mtf_block)
        # inverse BWT
        plain = inverse_bwt(last_col, stop_index)
        out.extend(plain)

        # If last block but there are residual bytes (shouldn't happen), error
        if last_block and off < temp_len:
            raise ValueError("Unexpected extra data after last block")

    # 5) Write result
    fout.write(out)

# -------------------- CLI --------------------
def main():
    ap = argparse.ArgumentParser(description="Decompress files produced by the provided WackBzip2 compressor.")
    ap.add_argument("input", help="*.wackbzip2 file")
    ap.add_argument("output", help="output file")
    ap.add_argument("--blocksize", type=int, default=512, help="MAX_BLOCKSIZE used during compression (default: 512)")
    args = ap.parse_args()

    with open(args.input, "rb") as fin, open(args.output, "wb") as fout:
        decompress_wackbzip2(fin, fout, args.blocksize)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
