from PIL import Image

# Open the text file and read the contents into a list of strings
with open("encrypted.txt", "r") as file:
    lines = file.readlines()

# Create an empty image with the same dimensions as the text file
width = len(lines[0].split())
height = len(lines)
image = Image.new("RGB", (width, height), (255, 255, 255))

# Iterate over the list of strings and set the corresponding pixels in the image
for y in range(height):
    for x, num in enumerate(lines[y].split()):
        # Convert the number to its binary representation and count the number of ones
        binary = bin(int(num))
        ones = binary.count("1")

        # If the number of ones is odd, set the pixel to black. Otherwise, set it to white.
        if ones % 2 == 1:
            image.putpixel((x, y), (0, 0, 0))
        else:
            image.putpixel((x, y), (255, 255, 255))

# Display the image
image.show()