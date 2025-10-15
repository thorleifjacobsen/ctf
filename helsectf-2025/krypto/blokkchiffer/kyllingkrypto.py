from math import sin

byte_string_containing_flag = b"helsectf{}"


def encrypt_chunk(plaintext, iv, key):
    xored = bytes(a ^ b for a, b in zip(plaintext, iv))
    xored_as_int = int.from_bytes(xored, 'big')
    key_as_int = int.from_bytes(key, 'big')
    ct = int(xored_as_int**(key_as_int/2**32 + 0.5)+sin(key_as_int)*1337)
    return ct.to_bytes(6, 'big')


def encrypt_bytes(plaintext, iv, key):
    ciphertext = bytes()
    ciphertext += iv
    for i in range(0, len(plaintext), 4):
        plain_chunk = plaintext[i:i+4]
        while len(plain_chunk) < 4:
            plain_chunk += b' '
        encrypted_chunk = encrypt_chunk(plain_chunk, iv, key)
        print(plain_chunk.hex(), encrypted_chunk.hex(), iv, key)
        ciphertext += encrypted_chunk
        iv = encrypted_chunk[-4:]
    return ciphertext


def main():
    # IV was chosen randomly by counting clucks in one hour
    iv = 0xdec0de17.to_bytes(4, 'big')
    # Key is not chosen randomly. Key is eggfaced!
    key = 0xe66faced.to_bytes(4, 'big')
    ciphertext = encrypt_bytes(byte_string_containing_flag, iv, key)
    print(ciphertext.hex())


if __name__ == "__main__":
    main()


# Output fra dette scriptet var:
# dec0de170d4d0f638c17029b2fa6f66b047042d4e1f7033834e1ccc10605de569aef1099391c765f06e568b1ed8804ced8024aa60fd0df478a8311e566838e17000d67d12005000c81e62f0f0eab36e358bc04813fa85e170672d47181af0f3f74ad3c5000020d0805a505b6b33574fc131fef636214
