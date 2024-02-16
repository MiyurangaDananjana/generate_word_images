from PIL import Image, ImageDraw, ImageFont
import os
import random
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
    text_height = text_size[3] - text_size[1]

    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=font_color)

    # Save the image
    image_filename = os.path.join(output_directory, f"{text}.png")
    image.save(image_filename)


# Create a directory to store the images
output_directory = "text_images"
os.makedirs(output_directory, exist_ok=True)

# Color list
color_list = [
    (47, 197, 181),
    (158, 208, 194),
    (65, 152, 116),
    (57, 133, 101),
    (208, 180, 141),
]

# Updated image size
image_size = (150, 80)

# Font settings
font_size = 30
font_color = (255, 255, 255)  # RGB color for white
font_filename = "ariblk.ttf"  # Change this to the font filename

# Check if the font file is valid
font_path = os.path.join("fonts", font_filename)
if not os.path.isfile(font_path):
    print(f"Error: Font file '{
          font_filename}' not found in the 'fonts' folder.")
    exit()

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except OSError as e:
    print(f"Error: Unable to load font file '{font_filename}': {e}")
    exit()

# List of custom texts
custom_texts = ["TXT", "DOC", "DOCX", "ODT", "MSG",
                "XLS", "XLSX", "ODS", "PPT", "PNG", "GIF", "SVG","PDF", "MSG"]

# Generate images with custom texts
for text in custom_texts:
    generate_image(text, output_directory, font,
                   image_size, font_color, color_list)

# Print the font information after generating images
print("Font information:", font)
print(f"Images generated and saved in the '{output_directory}' directory.")
