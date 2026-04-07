from colorsys import rgb_to_hls, hls_to_rgb

def rgb_tuple_to_int(rgb: tuple[int, int, int]) -> int:
    return rgb[0] << 16 | rgb[1] << 8 | rgb[2]

# https://stackoverflow.com/a/49601444
def adjust_lightness(color, amount=0.5) -> tuple[int, int, int]:
    color = map(lambda x: x / 255, color)
    color = rgb_to_hls(*color)

    return tuple(
        map(
            lambda x: int(x * 255),
            hls_to_rgb(color[0], max(0, min(1, amount * color[1])), color[2])
        )
    )

def darken_color(rgb: tuple[int, int, int]) -> tuple[int, int, int]:
    return adjust_lightness(rgb, 0.4)

def lighten_color(rgb: tuple[int, int, int]) -> tuple[int, int, int]:
    return adjust_lightness(rgb, 1.6)