import hashlib
import binascii

device_name = "DUCK9FEDF9"

flags_data = {
    'easy': {}, 'comms': {}, 'credits': {},
    'firmware': {}, 'authorized': {}, 'respond': {}, 'secured': {}
}

def last_5_characters_of_hash(text):
    hash_object = hashlib.sha256(text.encode())
    hash_bytes = hash_object.digest()
    hex_digest = binascii.hexlify(hash_bytes).decode('utf-8')      
    return hex_digest[-5:].upper()

def to_leet(text):
    leet_mapping = {
        'A': '4', 'B': '8', 'E': '3', 'G': '9', 'L': '1',
        'O': '0', 'S': '5', 'T': '7', 'Z': '2'
    }
    return ''.join(leet_mapping.get(char.upper(), char) for char in text)

for index, flag in enumerate(flags_data):
    flag_data = to_leet(f"{flag}_{index+1}".upper().replace("-", ""))
    if( flag == 'credits' ):
        print(f"DUCK_{flag_data}_01234")
    elif( flag == 'firmware' ):
        print(f"DUCK_{flag_data}_56789")
    elif( flag == 'easy' ):
        print(f"DUCK_{flag_data}_4612")
    else:
        for i in range(1, 8):
            flag_data = to_leet(f"{flag}_{i}".upper().replace("-", ""))
            device_id = device_name.replace("DUCK", "")
            suffix = last_5_characters_of_hash(f"DUCK_{device_id}_{flag_data}")
            flag_value = f"DUCK_{device_id}_{flag_data}_{suffix}"
            print(flag_value)
