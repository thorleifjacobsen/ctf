from pwn import *
import itertools


# Set log level to 'error' to remove debug output
context.log_level = 'error'

# Load elf
elf = ELF("./hvitboks", checksec=True)

# Define the characters to generate combinations from
characters = "abcdefghijklmnopqrstuvwxyz"

# Generate all combinations of 3 characters
combinations = itertools.product(characters, repeat=3)


# Loop through each combination and print
for combination in combinations:
    p = process(elf.path)
    password = "".join(combination).encode()

    print(f"Combination: {password}", end='\r')


    # Send password and receive response
    p.sendline(password)
    res = p.recvall().decode()

    if res.find("Feil") == 0:
      print()
      print("Correct: ", password)
      break

    # Check if process exited or not
    if p.poll() is not None:
        continue  # Break the loop if process exited

    # Close the process before restarting
    p.close()