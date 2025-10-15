# sign_remote_island_decoder.py

def hex_string_to_bytes(hex_str: str) -> bytes:
    """Convert a comma-separated hex string to bytes."""
    return bytes(int(h, 16) for h in hex_str.split(","))

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR two equal-length byte arrays."""
    return bytes(x ^ y for x, y in zip(a, b))

def main():
    text_hex = "2c,6a,3d,1f,72,fe,c5,ba,d3,26,f7,49,67,5b,ba,83,85,a8,f6,9c,31,23,18,cc,7c,b2,7b,8b,db,24,68,e3,8b,73,5c,a7,27,30,41,50,87,00,9a"
    xor_hex  = "0e,5e,0b,21,5c,cd,fc,96,d9,1b,c3,7f,59,51,98,b7,bc,91,fc,a1,05,15,26,c6,46,95,71,ad,e1,1c,58,c2,b6,4f,67,95,2d,00,78,76,b7,6a,b2"

    text_bytes = hex_string_to_bytes(text_hex)
    xor_bytes_ = hex_string_to_bytes(xor_hex)

    # Create 42 bytes of 0x55 (as in the GDScript)
    pad = bytes([0x55] * 42)

    first = xor_bytes(xor_bytes_, pad)
    result = xor_bytes(text_bytes, first)

    print(result.decode('utf-8'))

if __name__ == "__main__":
    main()
