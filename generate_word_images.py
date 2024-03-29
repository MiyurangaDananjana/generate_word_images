from PIL import Image, ImageDraw, ImageFont
import os
import random
import itertools
import string


def generate_image(text, output_directory, font, image_size, font_color, color_list):
    # Randomly select a background color from the list
    background_color = random.choice(color_list)

    # Create a new image with the selected background color
    image = Image.new("RGB", image_size, background_color)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Calculate text size and position to center it in the image
    text_size = draw.textbbox((0, 0), text, font)
    text_width = text_size[2] - text_size[0]
    text_height = text_size[2] - text_size[0]

    x = (image_size[0] - text_width) // 2
    y = (image_size[0] - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=font_color)

    # Save the image
    image_filename = os.path.join(output_directory, f"{text}.png")
    image.save(image_filename)


# Create a directory to store the images
output_directory = "word_images_2"
os.makedirs(output_directory, exist_ok=True)

# Color list
color_list = [
    (250, 250, 110),
    (196, 236, 116),
    (146, 220, 126),
    (100, 201, 135),
    (57, 180, 142),
    (8, 159, 143),
    (0, 137, 138),
    (8, 115, 127),
    (33, 93, 110),
    (42, 72, 88)
]

# Image size
image_size = (50, 50)

# Font settings
font_size = 16
font_color = (255, 255, 255)  # RGB color for white
font_filename = "ariblk.ttf"  # Change this to the font filename

# Check if the font file is valid
font_path = os.path.join("fonts", font_filename)
if not os.path.isfile(font_path):
    print(
        f"Error: Font file '{font_filename}' not found in the 'fonts' folder.")
    exit()

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except OSError as e:
    print(f"Error: Unable to load font file '{font_filename}': {e}")
    exit()

# Generate images for all possible two-letter words
for combination in itertools.product(string.ascii_uppercase, repeat=2):
    word = "".join(combination)
    generate_image(word, output_directory, font,
                   image_size, font_color, color_list)

# Print the font information after generating images
print("Font information:", font)

print(f"Images generated and saved in the '{output_directory}' directory.")
