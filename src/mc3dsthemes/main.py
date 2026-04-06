from .block_functions import render_rectangle_img, get_block_img, average_block_color
from PIL import Image

# Top screen x,z coords
top_start_xz = (-8, 6)
top_end_xz = (-32,-8)

# Bottom screen x,z coords
bottom_start_xz = (-11,-12)
bottom_end_xz = (-30, -26)

# TEMP: Just keeping this for now, will probs change to a config.toml file
overworld_path = "/home/intedai/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/26.1.1/minecraft/saves/3ds theme maker/dimensions/minecraft/overworld/region/"

# Icon part will be moved from main in the future
icon_xyz = (-30, -63, -30)

icon_mc_texture = get_block_img(overworld_path, *icon_xyz)
icon = icon_mc_texture.resize((48, 48), Image.NEAREST)
small_icon = icon_mc_texture.resize((24, 24), Image.NEAREST)

icon.show()
small_icon.show()

print(f"Red wool average color: {hex(average_block_color("red_wool"))}")

render_rectangle_img(overworld_path, top_start_xz, top_end_xz).show()
render_rectangle_img(overworld_path, bottom_start_xz, bottom_end_xz).show()