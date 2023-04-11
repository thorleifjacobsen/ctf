from Crypto.Util.number import isPrime
import struct
import base64

# Import pem formatted key
key_data = open('id_rsa', 'rb').read()

# find the start and end of the key data
start = key_data.find(b'\n') + 1
end = key_data.find(b'\n-----', start)
# extract the key data and remove any newlines
key_bytes = key_data[start:end].replace(b'\n', b'')
# decode the key data from base64
key_bytes = bytearray(base64.b64decode(key_bytes))

# Skip a few bytes
key_bytes = key_bytes[15:] #automagic
key_bytes = key_bytes[8:] #ciphername
key_bytes = key_bytes[8:] #kdfname
key_bytes = key_bytes[4:] #kdf
key_bytes = key_bytes[4:] #numb of keys, always 0
key_bytes = key_bytes[4:] # pubkey length

# Get key type
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("keytype: ", key_bytes[:length].decode()) # public key length
key_bytes = key_bytes[length:]

# Get pub0
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("pub0: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Get pub1
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("pub1: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

key_bytes = key_bytes[4:] # Skip length for rnd,prv,comment,pad

# A random 32bit int repeated
print("dummy: ", key_bytes[:8].hex()) 
key_bytes = key_bytes[8:]

# Key type private key
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("keytype: ", key_bytes[:length].decode()) 
key_bytes = key_bytes[length:]

# Pub0
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("pub0: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Pub1
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("pub1: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Prv 0
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("prv0: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Prv 1
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("prv1: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Prv 2
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("prv2: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Prv 3
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("prv3: ", key_bytes[:length].hex()) 
key_bytes = key_bytes[length:]

# Comment
length = int.from_bytes(key_bytes[:4], byteorder='big')
key_bytes = key_bytes[4:]
print("comment: ", key_bytes[:length].decode()) 
key_bytes = key_bytes[length:]

