from binascii import unhexlify, hexlify
import requests

def askOracle(ciphertext):
    """Sends a ciphertext to the server and returns True if the server returns a 200 status code,
    or False if the server returns a 400 status code."""

    response = requests.post("http://motherload.td.org.uit.no:8004", data=ciphertext)
    print(f"\r{hexlify(ciphertext).decode()} - {response.status_code}", end='')

    if response.status_code == 200:
        return True
    elif response.status_code == 400:
        return False
    else:
        raise ValueError("Unexpected status code: {}".format(response.status_code))


hex_string = "59f012ccb45de7ee596b87e45af712329b25d04e385791c61d72f84f3689556214bb965440c47ac87705e0cf0411d334e0089dd34c77f40df23653d3ba3e31b1e02c4a1f56d3bbf430b4b52427aa3a6a191475a6f737361fe6d13808f229c8f4"
ciphertext = bytearray(unhexlify(hex_string))
block_size = 16
num_blocks = int(len(ciphertext) / 16)

# initialize the plaintext to an empty binary array
plaintext = bytearray() 

# iterate over the blocks in reverse order
for block_num in range(num_blocks - 1, -1, -1): 

    if block_num == 0: 
        print("Skipping first block as we do not have data for it")
        break

    print(f"Starting with block: {block_num+1} of {num_blocks}")
    current_block = ciphertext[block_num*block_size:(block_num+1)*block_size]
    
    # initialize a intermediate state array.
    intermediate_state = [0] * block_size

    # iterate over the bytes of current block in reverse order
    for byte_num in range(block_size - 1, -1, -1):  

        padding_value = block_size - byte_num

        # Try each possible byte value in the current byte position of the test block
        for byte_guess in range(256):
            
            # Create a test block to extract the intermediate 
            test_block = [0] * block_size
            test_block[byte_num] = byte_guess
            
            # We need to fill the rightmost bytes with a XOR'ed padding_value for that intermediate state block.
            for i in range(byte_num, block_size):
                if intermediate_state[i] != 0: 
                    test_block[i] = intermediate_state[i] ^ padding_value

            if askOracle(bytes(test_block) + bytes(current_block)):
                
                # We now found the intermediate state of this block at this position.
                intermediate_state[byte_num] = padding_value ^ byte_guess
                # print()
                # print(f"Found intermediate state value: {hex(intermediate_state[byte_num])} - On guessed byte: {hex(byte_guess)}")
                
                # Lets calculate the decrypted byte for this block and byte number
                previousBlockByteAtSameLocation = ciphertext[(block_num-1)*block_size:block_num*block_size]
                plaintext.insert(0, intermediate_state[byte_num]^previousBlockByteAtSameLocation[byte_num])

                break
    print() # Just to add newline

print("=======================")
print("Decoded data:")
# Decode from byte to ascii, strip whitespaces, 
# reverse text and there you go!
print(plaintext.decode().strip())
print("=======================")
