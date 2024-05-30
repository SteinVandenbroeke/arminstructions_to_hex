from PIL import Image


def convert_image_to_c_array(image_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB format

    # Get the width and height of the image
    width, height = img.size

    # Initialize the array
    c_array = []

    # Process the image
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            hex_color = (r << 16) + (g << 8) + b  # Combine the RGB values into a single integer
            row.append(f"0x{hex_color:06X}")  # Format as 0xRRGGBB
        c_array.append(row)

    # Convert the array to a C style array string
    c_array_str = "int image_array[{}][{}] = {{".format(height, width)
    for row in c_array:
        c_array_str += "    {" + ", ".join(row) + "},"
    c_array_str += "};"

    return c_array_str


# Example usage
image_path = "pause-octagon-custom.png"
c_array_str = convert_image_to_c_array(image_path)
print(c_array_str)