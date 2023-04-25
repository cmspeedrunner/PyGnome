from PIL import Image
import random
import sys
file = str(sys.argv[1])

    
with open(file, "r") as f:
    input_string = f.read()
    f.close()

max_width = 500

# Define color palette for numbers 0-9
colors = [
    (255, 255, 255),  # 0: White
    (0, 0, 0),        # 1: Black
    (255, 0, 0),      # 2: Red
    (0, 255, 0),      # 3: Green
    (0, 0, 255),      # 4: Blue
    (255, 255, 0),    # 5: Yellow
    (0, 255, 255),    # 6: Cyan
    (255, 0, 255),    # 7: Magenta
    (128, 128, 128),  # 8: Gray
    (128, 0, 128),    # 9: Purple
]

# Determine width and height of the image based on input string length
input_length = len(input_string)
width = min(max_width, input_length)
height = (input_length + max_width - 1) // max_width

# Create a new blank image with a white background
image = Image.new("RGB", (width, height), "white")
pixels = image.load()  # Get the pixel data

# Draw pixels on the image based on input string and color palette
for i in range(input_length):
    char = input_string[i]
    x = i % max_width
    y = i // max_width
    color_index = int(char) % 10  # Map number 0-9 to color index
    color = colors[color_index]
    pixels[x, y] = color

# Save the image as .png
image.save("out.png")
