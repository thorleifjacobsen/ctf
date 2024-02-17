# The Rijndael Sbox from https://github.com/jacksoninfosec/rijndael-s-box/blob/main/rijndael_sbox.py


# x and y are nonnegative integers 
# Their associated binary polynomials are multiplied. 
# The associated integer to this product is returned. 
def multiply_ints_as_polynomials(x, y):
	z = 0
	while x != 0:
		if x & 1 == 1:
			z ^= y
		y <<= 1
		x >>= 1
	return z


# Returns the number of bits that are used 
# to store the non-negative integer x.
def number_bits(x):
	nb = 0
	while x != 0:
		nb += 1
		x >>= 1
	return nb


# x is a nonnegative integer
# m is a positive integer
def mod_int_as_polynomial(x, m):
	nbm = number_bits(m)
	while True:
		nbx = number_bits(x) 
		if nbx < nbm:
			return x
		mshift = m << (nbx - nbm)
		x ^= mshift


# x,y are 8-bits
# The output value is 8-bits
def rijndael_multiplication(x, y):
	z = multiply_ints_as_polynomials(x, y)
	m = int('100011011', 2)
	return mod_int_as_polynomial(z, m)


# x is 8-bits
# The output value is 8-bits
# Here we find the inverse just through a brute force search.
def rijndael_inverse(x):
	if x == 0:
		return 0
	for y in range(1, 256):
		if rijndael_multiplication(x, y) == 1:
			return y


# x, y are nonnegative integers 
# considered as vectors of bits
def dot_product(x, y):
	z = x & y
	dot = 0  
	while z != 0:
		dot ^= z & 1
		z >>= 1
	return dot 


# A is a 64-bit integer that represents a
# 8 by 8 matrix of 0's and 1's
# x and b are 8-bit integers, considered as column vectors
# This function calculates A * x + b
def affine_transformation(A, x, b):
	y = 0
	for i in reversed(range(8)):
		row = (A >> 8 * i) & 0xff 
		bit = dot_product(row, x)
		y ^= (bit << i)
	return y ^ b


# The input value x and the output value
# of the function are both 8-bit integers
def rijndael_sbox(x):
	xinv = rijndael_inverse(x)
	A = int('1111100001111100001111100001111110001111110001111110001111110001', 2)
	b = int('01100011', 2)
	return affine_transformation(A, xinv, b)

# Print the Rijndael S-Box as a table of 16 rows, 
# with 16 values per row (total of 256 values)
def print_rijndael_sbox():
	for row in range(16):
		for col in range(16):
			x = 16 * row + col
			hexstring = format(rijndael_sbox(x), "02x")
			print(hexstring, end=' ')
		print()

# Construct the Rijndael S-Box	
def construct_s_box():
    s_box = []
    for row in range(16):
        s_box.append([])
        for col in range(16):
            x = 16 * row + col
            s_box[row].append(rijndael_sbox(x))
    return s_box


# Brute the flag
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!#$%&'()*+,-./:;<=>?@[]^`{|}~"
flag_enc = "fc f9 20 52 ef fb 7f 23 18 21 aa b6 92 4d 3c ef 8f 92 4d 40 cf 40 f9 2 9f 43 ef 4d 50 ff".split(" ")
s_box = construct_s_box()

while len(flag_enc) > 0:
	for i in range(len(characters)):
		char = characters[i]
		char_enc = hex(s_box[ord(char) // 16][ord(char) % 16])[2:]

		if char_enc == flag_enc[0]:
			print(char, end="")
			flag_enc.pop(0)
			break