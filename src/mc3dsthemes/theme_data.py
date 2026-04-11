from PIL import Image
from pathlib import Path
from .block_funcs import render_rectangle_img, get_block_img, average_block_color
from .rc_funcs import make_color_dict
from .text_generator import TextGenerator
import datetime as dt
from calendar import day_abbr

ASSETS_PATH = Path(__file__).parent / "assets"
FONTS_PATH = ASSETS_PATH / "fonts"
FONT_PATH = FONTS_PATH  / "Ubuntu-Regular.ttf"
SCREEN_IMG_SIZE = (512, 256)

# Top screen
TOP_START_X_Z = (-8, 6)
TOP_END_X_Z = (-32,-8)
TOP_PASTE_POS = (6, 0)
TOP_SCREEN_FILE_NAME = "top.png"

# Bottom screen
BOTTOM_START_X_Z = (-11,-12)
BOTTOM_END_X_Z = (-30, -26)
BOTTOM_PASTE_POS = (0, 0)
BOTTOM_SCREEN_FILE_NAME = "bottom.png"

# Icon
ICON_X_Y_Z = (-30, -63, -30)
ICON_SIZE = (48, 48)
ICON_FILE_NAME = "icon.png"
SMALL_ICON_SIZE = (24, 24)
SMALL_ICON_FILE_NAME = "small_icon.png"

def create_icons(output_dir: Path, overworld_path: Path) -> None:
    icon_mc_texture = get_block_img(overworld_path, *ICON_X_Y_Z)
    
    icon = icon_mc_texture.resize(ICON_SIZE, Image.NEAREST)
    small_icon = icon_mc_texture.resize(SMALL_ICON_SIZE, Image.NEAREST)

    icon.save(output_dir / ICON_FILE_NAME)
    small_icon.save(output_dir / SMALL_ICON_FILE_NAME)

def render_minecraft_screens(overworld_path: Path) -> tuple[Image.Image, Image.Image]:
    top_minecraft_render = render_rectangle_img(overworld_path, TOP_START_X_Z, TOP_END_X_Z)
    bottom_minecraft_render = render_rectangle_img(overworld_path, BOTTOM_START_X_Z, BOTTOM_END_X_Z)

    return top_minecraft_render, bottom_minecraft_render

def create_screen_imgs(top_minecraft_render: Image.Image, bottom_minecraft_render: Image.Image, output_dir: Path) -> None:
    top_final = Image.new("RGB", SCREEN_IMG_SIZE)
    bottom_final = Image.new("RGB", SCREEN_IMG_SIZE)

    top_final.paste(top_minecraft_render, TOP_PASTE_POS)
    bottom_final.paste(bottom_minecraft_render, BOTTOM_PASTE_POS)

    top_final.save(output_dir / TOP_SCREEN_FILE_NAME)
    bottom_final.save(output_dir / BOTTOM_SCREEN_FILE_NAME)

def make_final_color_dict():
    #make_color_dict(params) using average colors and const coords above
    pass

def create_preview_img(top_minecraft_render: Image.Image, bottom_minecraft_render: Image.Image, output_dir: Path) -> None:
    top_w, top_h = top_minecraft_render.size
    bottom_w, bottom_h = bottom_minecraft_render.size

    preview = Image.new("RGBA", (top_w, top_h + bottom_h))

    top_info_overlay = Image.open(ASSETS_PATH / "top_info_overlay.png")
    bottom_center_buttons = Image.open(ASSETS_PATH / "bottom_center_buttons.png")
    
    text_generator = TextGenerator(preview, FONT_PATH)

    preview.paste(top_minecraft_render, (0, 0))

    x_pos_bottom_screen = (top_w - bottom_w) // 2

    preview.paste(bottom_minecraft_render, (x_pos_bottom_screen, top_h))
    preview.alpha_composite(top_info_overlay, (0, 0))

    now = dt.datetime.now()
    top_info_text = now.strftime(f"300      %m/%d ({day_abbr[now.weekday()]})   %H:%M")

    text_generator.draw_outlined_text((168, 1), top_info_text, 16, (50, 50, 50), (255, 255, 255), 1)

    preview.alpha_composite(bottom_center_buttons, (x_pos_bottom_screen + 63, top_h))

    preview.save(output_dir / "preview.png")

#print(f"Red wool average color: {hex(average_block_color("red_wool"))}")