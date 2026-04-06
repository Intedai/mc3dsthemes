from .block_functions import render_rectangle_img, average_block_color

# Top screen x,z coords in the MC world
top_start_xz = (-8, 6)
top_end_xz = (-32,-8)

# Bottom screen x,z coords in the MC world
bottom_start_xz = (-11,-12)
bottom_end_xz = (-30, -26)

# TEMP: Just keeping this for now, will probs change to a config.toml file
overworld_path = "/home/intedai/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/26.1.1/minecraft/saves/3ds theme maker/dimensions/minecraft/overworld/region/"

render_rectangle_img(overworld_path, top_start_xz, top_end_xz).show()
render_rectangle_img(overworld_path, bottom_start_xz, bottom_end_xz).show()

print(f"Red wool average color: {hex(average_block_color("red_wool"))}")