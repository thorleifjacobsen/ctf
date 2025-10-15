#!/usr/bin/env python3
# solve_vig.py -- automatic solver for the challenge (keylen in 4..7, uppercase A-Z)
import socket
from collections import Counter
import math

HOST = "ctf.wackattack.eu"
PORT = 8086

# english letter frequency (A..Z) from typical corpora
EN_FREQ = {
 'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015,
 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749,
 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056, 'U': 2.758,
 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074
}

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(ALPH)

def chi_squared_score(s):
    """chi-sq statistic for s (A..Z) against EN_FREQ"""
    L = len(s)
    if L == 0: return float('inf')
    cnt = Counter(s)
    chi = 0.0
    for c in ALPH:
        obs = cnt.get(c,0)
        exp = EN_FREQ[c] * L / 100.0
        chi += (obs - exp) ** 2 / (exp + 1e-9)
    return chi

def best_shift_for_column(col):
    """Return shift (0..25) that produces lowest chi-sq when column is shifted back by shift."""
    best = None
    best_shift = 0
    for shift in range(N):
        # decrypt with shift: each cipher letter C -> P = (C - shift) % 26
        dec = ''.join(ALPH[(ALPH.index(ch) - shift) % N] for ch in col)
        score = chi_squared_score(dec)
        if best is None or score < best:
            best = score
            best_shift = shift
    return best_shift

def solve_vigenere(ct, min_k=4, max_k=7):
    ct = ''.join(ch for ch in ct.strip().upper() if ch in ALPH)
    best_plain = None
    best_score = None
    for k in range(min_k, max_k+1):
        key_shifts = []
        for i in range(k):
            col = ct[i::k]
            shift = best_shift_for_column(col)
            key_shifts.append(shift)
        # decrypt with found shifts
        pt = []
        for idx,ch in enumerate(ct):
            shift = key_shifts[idx % k]
            plain_ch = ALPH[(ALPH.index(ch) - shift) % N]
            pt.append(plain_ch)
        pt = ''.join(pt)
        # score the plaintext by chi-sq of whole text (lower is better)
        score = chi_squared_score(pt)
        if best_score is None or score < best_score:
            best_score = score
            best_plain = pt
    return best_plain

def recv_until(s, marker, timeout=5):
    buf = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        buf += chunk
        if marker.encode() in buf:
            break
    return buf.decode(errors="ignore")

def interact_and_solve():
    s = socket.create_connection((HOST, PORT))
    print(recv_until(s, "Are you ready?"))  # initial banner
    s.sendall(b"\n")  # press enter
    solved = 0
    while True:
        data = recv_until(s, "Here is some ciphertext")
        if not data:
            break
        # read the ciphertext line (it should follow)
        rest = s.recv(65536).decode(errors="ignore")
        # try to extract the CT line (first long uppercase line)
        lines = rest.splitlines()
        ct_line = None
        for ln in lines:
            ln = ln.strip()
            if ln and all(ch.isalpha() for ch in ln):
                # assume this is CT (A..Z)
                ct_line = ln
                break
        if ct_line is None:
            print("Couldn't find ciphertext, raw received:")
            print(rest)
            break
        pt_guess = solve_vigenere(ct_line)
        print(f"Guessed plaintext (first 60 chars): {pt_guess[:60]}...")
        # send plaintext guess
        s.sendall((pt_guess + "\n").encode())
        reply = recv_until(s, "That is correct")
        if "That is correct" in reply:
            solved += 1
            print(f"Solved {solved}")
            # continue to next iteration
            continue
        else:
            # maybe we got "That is not correct..." which reveals the key; print and exit
            print(reply)
            break

if __name__ == "__main__":
    interact_and_solve()
