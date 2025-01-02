import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)

def generate_complementary_colors(base_color):
    """Generate complementary color scheme based on a base color."""
    r, g, b = [x / 255.0 for x in hex_to_rgb(base_color)]
    
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    
    complementary_hue = (h + 0.5) % 1.0
    comp_r, comp_g, comp_b = colorsys.hls_to_rgb(complementary_hue, l, s)
    
    complementary_color = rgb_to_hex((int(comp_r * 255), int(comp_g * 255), int(comp_b * 255)))
    
    return complementary_color

base_color = input("Enter a base color in HEX format (e.g., #3498db): ").strip()

try:
    complementary_color = generate_complementary_colors(base_color)
    print(f"Base Color: {base_color}")
    print(f"Complementary Color: {complementary_color}")
except ValueError:
    print("Invalid HEX color format. Please try again.")
