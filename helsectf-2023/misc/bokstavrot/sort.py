from PIL import Image
import os

# Define the folder path where the images are located
folder_path = "./brev/"

# Array for images
images = []


# Loop through each file in the directory
for filename in os.listdir("./brev/"):
    
    # Open the image file
    image = Image.open(f'./brev/{filename}')
    
    # Get the color code of pixel 1x1
    color_code = image.getpixel((0, 0))
    
    # Add blue value and filename to array
    images.append((color_code[2], filename))

# Sort the images based on the color code value
images.sort(key=lambda x: x[0])

# Rename them for easee.
x=0
for image in images:

    os.rename(f'./brev/{image[1]}', f'./brev/{x}.png')
    x += 1
