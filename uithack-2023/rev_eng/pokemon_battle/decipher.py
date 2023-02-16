
def xor(data, key):
    return bytearray((a ^ b for a, b in zip(data,key)))

flag=b'a\x1a<#RT\x08ZF\x16SC\x1c\\Rh\x00\\B\x0e\\,[\x06l\x03\x0f\x04*\\\x01B\x15'
key = b'4shk37chum4shk37chum4shk37chum4sh'

print(xor(flag,key))