# One of the fast-lanes

The source code implies that the flags are generated on the fly, so all flags can be gathered from the source code. All you need to have is the `device id`.

There is a flag generator in the source which generates them based on a dictionary. But since MicroPython for some reason do not reliably predict the order based on the source you need to generate one based on each possible order position.

Here I've created a [solve.py](./solve.py) which bsaed on the device ID and flag names generates all possible flags:

```python
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
```

This gives:

```
DUCK_345Y_1_4612
DUCK_9FEDF9_C0MM5_1_771BF
DUCK_9FEDF9_C0MM5_2_0F9D6
DUCK_9FEDF9_C0MM5_3_C2B8C
DUCK_9FEDF9_C0MM5_4_A78AC
DUCK_9FEDF9_C0MM5_5_BC078
DUCK_9FEDF9_C0MM5_6_18A31
DUCK_9FEDF9_C0MM5_7_A0511
DUCK_CR3DI75_3_01234
DUCK_FIRMW4R3_4_56789
DUCK_9FEDF9_4U7H0RI23D_1_76915
DUCK_9FEDF9_4U7H0RI23D_2_CC4B0
DUCK_9FEDF9_4U7H0RI23D_3_F5BEF
DUCK_9FEDF9_4U7H0RI23D_4_830BF
DUCK_9FEDF9_4U7H0RI23D_5_C2CFF
DUCK_9FEDF9_4U7H0RI23D_6_97A11
DUCK_9FEDF9_4U7H0RI23D_7_B6BA5
DUCK_9FEDF9_R35P0ND_1_5EBCE
DUCK_9FEDF9_R35P0ND_2_43CDA
DUCK_9FEDF9_R35P0ND_3_F96F2
DUCK_9FEDF9_R35P0ND_4_5637C
DUCK_9FEDF9_R35P0ND_5_A5A4A
DUCK_9FEDF9_R35P0ND_6_D99C5
DUCK_9FEDF9_R35P0ND_7_FC322
DUCK_9FEDF9_53CUR3D_1_95519
DUCK_9FEDF9_53CUR3D_2_8D976
DUCK_9FEDF9_53CUR3D_3_98CC8
DUCK_9FEDF9_53CUR3D_4_BF795
DUCK_9FEDF9_53CUR3D_5_34327
DUCK_9FEDF9_53CUR3D_6_0656A
DUCK_9FEDF9_53CUR3D_7_0872F
```

Using this you can easily just input all flags without accessing the device over USB.


