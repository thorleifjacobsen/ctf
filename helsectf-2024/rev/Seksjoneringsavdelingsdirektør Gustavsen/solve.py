from pwn import *
import string

context.log_level = 'warn'

# Function to perform XOR operation
def xor(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

# Is printable
def isPrintable(bytes):
    for byte in bytes:
        if byte < 32 or 128 < byte:
            return False
    return True

# Process each ELF file in the current directory
elf = ELF("./gustavsen")

# Iterate through sections in the ELF file
for section in elf.iter_sections():
    # Get the data from the section
    section_data = section.data()

    # Assuming the magic number and key are the first 8 bytes
    magic = section_data[:4]
    key = section_data[4:8]
    data_to_xor = section_data[8:]

    # XOR the data with the key
    result = xor(data_to_xor, key)

    # Check if data contains unprintable characters
    if not isPrintable(result):
        continue

    result = result.decode()
    print(f"Section {section.name}: ", end="")
    print(result)
