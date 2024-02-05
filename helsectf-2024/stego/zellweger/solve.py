from PIL import Image, ImageSequence, ImageChops

# Load image
img = Image.open('./zellweger.png')

# Collect all the LSBs
bits = []
for pixel in list(img.getdata()):
    bits.append(pixel[0] & 0b00000001)
    bits.append(pixel[1] & 0b00000001)
    bits.append(pixel[2] & 0b00000001)

# Loop the bits until we get a 1 
skip = 1
for i in range(len(bits)):
    if skip > 0:
        skip -= 1
        continue

    if bits[i] == 1:
        decabit = bits[i+1:i+11]
        print(''.join(map(str, decabit)))
        skip = 11