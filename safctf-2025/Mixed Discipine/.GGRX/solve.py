from PIL import Image

img = Image.open("inspecturm_adjusted.png").convert('RGB')
width, height = img.size
pixels = img.load()

for x in range(15, width, 13):
    strongest_color = 0
    strongest_y = 0
    for y in range(height):
        color_sum = sum(pixels[x, y]) # Sum all RGB values if it is higher than 10 it is not black atleast.
        if strongest_color < color_sum:
            strongest_color = color_sum
            strongest_y = y
    
    if strongest_color < 10:
        continue
    
    if strongest_y > height / 2:
        print("0", end="")    
    else:
        print("1", end="")
    
print()
