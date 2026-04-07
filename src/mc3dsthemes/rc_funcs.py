import configparser
from pathlib import Path
from .color_funcs import rgb_tuple_to_int, lighten_color, darken_color

class Sections:
    info = "info"
    frames = "frames"
    textures = "textures"
    colors = "colors"
    flags = "flags"
    audio = "audio"

GENERATED_FILE_NAME = "config.rc"

def add_value(
    config: configparser.ConfigParser,
    section: str,
    key: str,
    value: str
):
    if not config.has_section(section):
        config.add_section(section)
    
    config[section][key] = str(value)

def add_values_dict(config: configparser.ConfigParser, section:str, values_dict: dict):
    for key, value in values_dict.items():
        add_value(config, section, key, value)

def add_color_to_dict(
    color_dict: dict,
    key: str,
    color: tuple,
):
    color_dict[key] = hex(rgb_tuple_to_int(color))

def add_colors_to_dict(
    color_dict: dict,
    key: str,
    color: tuple[int, int, int],
    add_dark: bool,
    add_light: bool,
    shadow: tuple[int, int, int] | None = None,
    glow: tuple[int, int, int] | None = None,
    textmain: tuple[int, int, int] | None = None,
    textselected: tuple[int, int, int] | None = None,
    textshadow: tuple[int, int, int] | None = None,
    textshadowpos: int | None = None
):
    add_color_to_dict(color_dict, f"{key}.main", color)
    if add_dark:
        add_color_to_dict(color_dict, f"{key}.dark", color)
    if add_light:
        add_color_to_dict(color_dict, f"{key}.light", color)
    if shadow:
        add_color_to_dict(color_dict, f"{key}.shadow", shadow)
    if glow:
        add_color_to_dict(color_dict, f"{key}.glow", glow)
    if textmain:
        add_color_to_dict(color_dict, f"{key}.textmain", textmain)
    if textselected:
        add_color_to_dict(color_dict, f"{key}.textselected", textselected)
    if textshadow:
        add_color_to_dict(color_dict, f"{key}.textshadow", textshadow)
    if textshadowpos:
        color_dict[f"{key}.textshadowpos"] = str(textshadowpos)
    
def make_color_dict(
    cursorcolor: tuple[int, int, int],
    cursorcolor_glow: tuple[int, int, int],
    foldercolor: tuple[int, int, int],
    foldercolor_shadow: tuple[int, int, int],
    filecolor: tuple[int, int, int],
    filecolor_shadow: tuple[int, int, int],
    arrowbuttoncolor: tuple[int, int, int],
    arrowbuttoncolor_shadow: tuple[int, int, int],
    arrowcolor_border: tuple[int, int, int],
    arrowcolor_unpressed: tuple[int, int, int],
    arrowcolor_pressed: tuple[int, int, int],
    open: tuple[int, int, int],
    open_shadow: tuple[int, int, int],
    open_glow: tuple[int, int, int],
    open_textshadow: tuple[int, int, int],
    open_text: tuple[int, int, int],
    open_textselected: tuple[int, int, int],
    close: tuple[int, int, int],
    close_shadow: tuple[int, int, int],
    close_glow: tuple[int, int, int],
    close_textshadow: tuple[int, int, int],
    close_text: tuple[int, int, int],
    close_textselected: tuple[int, int, int],  
    gametext: tuple[int, int, int],
    gametext_shadow: tuple[int, int, int],
    gametext_text: tuple[int, int, int],
    folderbgcolor: tuple[int, int, int],
    folderbgcolor_shadow: tuple[int, int, int],
    folderarrowcolor: tuple[int, int, int],
    folderarrowcolor_shadow: tuple[int, int, int],
    folderarrowcolor_glow: tuple[int, int, int],
    folderarrowcolor_text: tuple[int, int, int],
    folderarrowcolor_textshadow: tuple[int, int, int],
    folderarrowcolor_textselected: tuple[int, int, int],
    bottomcornerbuttoncolor: tuple[int, int, int],
    bottomcornerbuttoncolor_shadow: tuple[int, int, int],
    bottomcornerbuttoncolor_icon: tuple[int, int, int],
    bottomcornerbuttoncolor_icontext: tuple[int, int, int],
    topcornerbuttoncolor: tuple[int, int, int],
    topcornerbuttoncolor_shadow: tuple[int, int, int],
    topcornerbuttoncolor_text: tuple[int, int, int],
    demotextcolor: tuple[int, int, int],
    demotextcolor_text: tuple[int, int, int]
):
    
    color_dict = {}

    add_colors_to_dict(
        color_dict,
        "cursorcolor",
        cursorcolor,
        True,
        True,
        None,
        cursorcolor_glow
    )
    add_colors_to_dict(
        color_dict,
        "foldercolor",
        foldercolor,
        True,
        True,
        foldercolor_shadow,
        None
    )
    add_colors_to_dict(
        color_dict,
        "filecolor",
        filecolor,
        True,
        True,
        filecolor_shadow,
        None
    )
    add_colors_to_dict(
        color_dict,
        "arrowbuttoncolor",
        arrowbuttoncolor,
        True,
        True,
        arrowbuttoncolor_shadow,
        None
    )
    add_color_to_dict(color_dict, "arrowcolor.border", arrowcolor_border)
    add_color_to_dict(color_dict, "arrowcolor.unpressed", arrowcolor_unpressed)
    add_color_to_dict(color_dict, "arrowcolor.pressed", arrowcolor_pressed)
    add_colors_to_dict(
        color_dict,
        "open",
        open,
        True,
        True,
        open_shadow,
        open_glow,
        open_text,
        open_textselected,
        open_textshadow,
        textshadowpos=1
    )
    add_colors_to_dict(
        color_dict,
        "close",
        close,
        True,
        True,
        close_shadow,
        close_glow,
        close_text,
        close_textselected,
        close_textshadow,
        textshadowpos=1
    )
    add_colors_to_dict(
        color_dict,
        "gametext",
        gametext,
        False,
        True,
        gametext_shadow,
        None,
        gametext_text
    )
    add_colors_to_dict(
        color_dict,
        "folderbgcolor",
        folderbgcolor,
        True,
        True,
        folderbgcolor_shadow
    )
    add_colors_to_dict(
        color_dict,
        "folderarrowcolor",
        folderarrowcolor,
        True,
        True,
        folderarrowcolor_shadow,
        folderarrowcolor_glow,
        folderarrowcolor_text,
        folderarrowcolor_textselected,
        folderarrowcolor_textshadow,
        textshadowpos=1
    )
    add_colors_to_dict(
        color_dict,
        "bottomcornerbuttoncolor",
        bottomcornerbuttoncolor,
        True,
        True,
        bottomcornerbuttoncolor_shadow,
    )
    add_color_to_dict(color_dict, "bottomcornerbuttoncolor.iconmain", bottomcornerbuttoncolor_icon)
    add_color_to_dict(color_dict, "bottomcornerbuttoncolor.iconlight", lighten_color(bottomcornerbuttoncolor_icon))
    add_color_to_dict(color_dict, "bottomcornerbuttoncolor.icontextmain", bottomcornerbuttoncolor_icontext)
    add_colors_to_dict(
        color_dict,
        "topcornerbuttoncolor",
        topcornerbuttoncolor,
        False,
        True,
        topcornerbuttoncolor_shadow,
        None,
        topcornerbuttoncolor_text
    )
    add_colors_to_dict(
        color_dict,
        "demotextcolor",
        demotextcolor,
        False,
        False,
        None,
        None,
        demotextcolor_text
    )

    return color_dict


def make_rc_file(
    output_dir: Path,
    shorttitle: str,
    longtitle: str,
    publisher: str,
    color_dict: dict,
    game_text_hidden: bool,
    has_bgm: bool,
    bgm_path: Path | None = None

):
    config = configparser.ConfigParser()

    info_values = {
        "shorttitle": shorttitle,
        "longtitle": longtitle,
        "publisher": publisher,
        "icon": "icon.png",
        "smallicon": "small_icon.png"
    }
    add_values_dict(config, Sections.info, info_values)

    frames_values = {
        "top.type": "texture",
        "top.frame": "single",
        "bottom.type": "texture",
        "bottom.frame": "single"
    }
    add_values_dict(config, Sections.frames, frames_values)

    textures_values = {
        "top.image": "top.png",
        "bottom.image": "bottom.png"
    }
    add_values_dict(config, Sections.textures, textures_values)

    add_values_dict(config, Sections.colors, color_dict)
    if game_text_hidden:
        add_value(
            config,
            Sections.flags,
            "gametext.hidden",
            "Herobrine" # Any value if hidden
        )
    
    if has_bgm and bgm_path:
        add_value(
            config,
            Sections.audio,
            "bgm",
            bgm_path
        )
    
    with open(output_dir / GENERATED_FILE_NAME, 'w') as configfile:
        configfile.write("; rc file for kame-tools generated by mc3dstheme\n\n")
        config.write(configfile)