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
    
    # Process to remove black background
    datas = frame.getdata()
    newData = []
    threshold = 10  # Anything below 10 in r g or b is considered black
    for item in datas:
        # Change all pixels that are pure black to transparent
        if item[0] <= threshold and item[1] <= threshold and item[2] <= threshold:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
    
    # Update frame data
    frame.putdata(newData)
    frames.append(frame)

# Create a new image with a white background
merged_image = Image.new('RGBA', gif.size, (0, 0, 0, 0))

# Paste the frames next to each other
print(f"Number of frames: {len(frames)}")
for frame in frames:
    merged_image = Image.alpha_composite(merged_image, frame)

# Save the result
merged_image_path = './merged_image.png'
merged_image.save(merged_image_path)