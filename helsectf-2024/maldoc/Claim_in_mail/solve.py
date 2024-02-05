import base64

def b64_decode(encoded_string, key):
    # Decode the Base64 encoded string
    byte_array = base64.b64decode(encoded_string)

    # Calculate the number used in XOR operation
    num = (key * 2686 + 1432990190) % 256

    # Perform XOR operation on each byte
    decrypted_bytes = bytearray()
    for byte in byte_array:
        decrypted_bytes.append(byte ^ num)

    # Convert the byte array to a UTF-8 string
    return decrypted_bytes.decode('utf-8')

# Example usage
encoded_string = "DAEIFwEHEAIfDQI7DRA7FQUPFzsIDQ8BOwU7BgsQO1IBBgBTAVxSAgVRBVxWAgZUUlZcVFQCXVFWXQIBAAFQVFYFBlAGU1FcUFFXAQFVUFFSVV1TU1FQBwVUUVVVUFEZ"
key = 5  # Replace with your key
decoded_string = b64_decode(encoded_string, key)
print(decoded_string)
