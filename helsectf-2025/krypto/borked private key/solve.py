#!/usr/bin/env python3
import time

# Flips exactly one bit in the given bytes object and yields the result (as bytes).
def flip_one_bit(bdata):
    barray = bytearray(bdata)
    for i in range(len(barray)):
        for bit in range(8):
            mask = 1 << bit
            barray[i] ^= mask    # flip this one bit
            yield bytes(barray)
            barray[i] ^= mask    # flip it back

def bytes_to_int(b):
    return int.from_bytes(b, 'big')

if __name__ == "__main__":
    # The three values each have exactly 1 bit wrong.
    # Provided as hex or set them however you want:
    n_hex = "00a747f22ebd523ab3a3420b395fed6082debcf05cfcae23c54dc270f90d7c56d00cbfed5651abb9d041aca43fd386dc24518fd51db96544af29bd819d7290ad00e2fe01434b1423d113e6a8228ad82965fb8d04f1288447a9d97f8bfe2aa04931cda5beafd0886bfde16523584543af6833b8aa810cd49d0d74e45a423b87e61f349b35e560261b2d458fc674447676e880b72a62ef675296dd941972d3a0927336cd47034da02ea2de03960376927699efb18aa7f672a9ade2f2d8461b576bc3c6be3d21dbb3f860e8bf1983d01e9b192d8a4dcb8367dd124c84fff66ba62f177d22c908fc4b2be0dc3212c8db95b0e23d54c23e880d2454f45c011338609067"
    p_hex = "00bb9c2fb22dc5b5f16518fbe19408fba15e9bbc6eb699c88e87bf81fa152888d653a43cb3b3f77d037045cbeaaba4444d026016f4000c6db312844638756cf4181954336a3e8ab252e7f135a8d8d39dd5490574540ffb1cf4a411e06d6cd717fa6679f8790d001580af97473a48998bd5b514015f39787c34f7b3358dab5526db"
    q_hex = "00e442a5343c1e82347b01c59050d2e29987e8fa8347969efde9eb9d9b215ce9ae1c9bc6d377d9d887bded0d0944ae58190ea75d52413868aba64bcc39912c3727a46f64d9e37d08423d7eb67ebaff103a062017ddab02339a16f4955d8358620fd737a77e0e25bbab047a6417d720796ebe1e7345b892d3661947dddb0d977465"

    n_b = bytes.fromhex(n_hex)
    p_b = bytes.fromhex(p_hex)
    q_b = bytes.fromhex(q_hex)

    # For progress
    flips_n = len(n_b)*8
    flips_p = len(p_b)*8
    flips_q = len(q_b)*8
    total = flips_n * flips_p * flips_q
    iteration = 0
    start_time = time.time()

    # Triple nested loop: try flipping exactly 1 bit in n, p, q and check p'*q' == n'
    for n_idx, n_flipped in enumerate(flip_one_bit(n_b)):
        n_int_flipped = bytes_to_int(n_flipped)
        for p_idx, p_flipped in enumerate(flip_one_bit(p_b)):
            p_int_flipped = bytes_to_int(p_flipped)
            for q_idx, q_flipped in enumerate(flip_one_bit(q_b)):
                q_int_flipped = bytes_to_int(q_flipped)

                iteration += 1
                if iteration % 10000 == 0:
                    elapsed = time.time() - start_time
                    done_ratio = iteration / total
                    eta = (elapsed / iteration) * (total - iteration)
                    print(f"\rProgress: {done_ratio*100:.2f}%  |  ETA: ~{eta:.1f}s", end="")

                # Check if this combination fixes them: p'*q' == n'
                if p_int_flipped * q_int_flipped == n_int_flipped:
                    print("\nFound corrected values!")
                    print(f"Corrected n: {hex(n_int_flipped)}")
                    print(f"Corrected p: {hex(p_int_flipped)}")
                    print(f"Corrected q: {hex(q_int_flipped)}")
                    print(f"Flipped bit in n (index {n_idx})")
                    print(f"Flipped bit in p (index {p_idx})")
                    print(f"Flipped bit in q (index {q_idx})")
                    exit(0)

    print("\nNo single-bit fix found for all three simultaneously.")
