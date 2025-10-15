from math import sin
from binascii import unhexlify

def decrypt_chunk(cipher_chunk, iv, key):
    key_as_int = int.from_bytes(key, 'big')
    cipher_as_int = int.from_bytes(cipher_chunk, 'big')

    xored_as_int = round((cipher_as_int - sin(key_as_int)*1337)**(1/(key_as_int/2**32 + 0.5)))
    xored_bytes = xored_as_int.to_bytes(4, 'big')

    plaintext = bytes(a ^ b for a, b in zip(xored_bytes, iv))
    return plaintext


def decrypt_bytes(ciphertext, key):
    iv = ciphertext[:4]
    plaintext = b''
    for i in range(4, len(ciphertext), 6):
        cipher_chunk = ciphertext[i:i+6]
        plaintext_chunk = decrypt_chunk(cipher_chunk, iv, key)
        plaintext += plaintext_chunk
        iv = cipher_chunk[-4:]
    return plaintext.rstrip(b' ')


ciphertext = unhexlify("dec0de170d4d0f638c17029b2fa6f66b047042d4e1f7033834e1ccc10605de569aef1099391c765f06e568b1ed8804ced8024aa60fd0df478a8311e566838e17000d67d12005000c81e62f0f0eab36e358bc04813fa85e170672d47181af0f3f74ad3c5000020d0805a505b6b33574fc131fef636214")
key = 0xe66faced.to_bytes(4, 'big')

flag = decrypt_bytes(ciphertext, key)
print(flag.decode())