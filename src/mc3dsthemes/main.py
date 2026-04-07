from shutil import rmtree
from pathlib import Path
from .theme_data import create_icons, render_minecraft_screens, create_screen_imgs, create_preview_img
from .rc_funcs import make_color_dict, make_rc_file
# TEMP: Just keeping this for now, will probs change to a config.toml file
OVERWORLD_PATH = "/home/intedai/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/26.1.1/minecraft/saves/3ds theme maker/dimensions/minecraft/overworld/region/"

def main():
    #author_name = input("Enter author name: ")
    
    temp_dir = Path("tmp")
    temp_dir.mkdir(exist_ok=True)

    create_icons(temp_dir, OVERWORLD_PATH)
    
    top_img, bottom_img = render_minecraft_screens(OVERWORLD_PATH)
    create_screen_imgs(top_img, bottom_img, temp_dir)

    # Temp creation with the same color in everything
    tmp_colors = [(247, 185, 220)] * 43
    color_dict = make_color_dict(*tmp_colors)
    make_rc_file(
        temp_dir,
        "short title",
        "long title",
        "publisher",
        color_dict,
        False,
        False
    )

    create_preview_img(top_img, bottom_img)

    if temp_dir.exists():
        #rmtree(temp_dir)
        pass

if __name__ == "__main__":
    main()