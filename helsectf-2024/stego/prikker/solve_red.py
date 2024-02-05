from PIL import Image, ImageSequence, ImageChops

# Load the GIF
gif_path = './prikker.gif'
gif = Image.open(gif_path)

# Extract frames and remove black background
frames = []
for frame in ImageSequence.Iterator(gif):
    print(f"Processing frame {len(frames) + 1} of {gif.n_frames}")

    # Convert to RGBA if necessary
    frame = frame.convert("RGBA")
    
    # Process to keep only the red pixels
    datas = frame.getdata()
    newData = []
    for item in datas:
        if item[0] > 100 and item[1] < 10 and item[2] < 10:
            newData.append(item)
        else:
            newData.append((0, 0, 0, 0))

    # Update frame data
    frame.putdata(newData)
    frames.append(frame) 

# Create a new image with a white background
merged_image = Image.new('RGBA', gif.size, (0, 137, 0, 255))

# Paste the frames next to each other
for frame in frames:
    merged_image = Image.alpha_composite(merged_image, frame)

# Save the result
merged_image_path = './merged_image_red_only.png'
merged_image.save(merged_image_path)