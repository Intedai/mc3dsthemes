from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

class TextGenerator:
    def __init__(
        self,
        img: Image.Image,
        font_path: Path,
    ):
        self.draw = ImageDraw.Draw(img)
        self.font_path = font_path
        self.font_size = None

    def change_font_size(self, font_size):
        if font_size != self.font_size:
            self.font_size = font_size
            self.font = ImageFont.truetype(self.font_path, font_size)

    def draw_text(
        self,
        pos: tuple[int, int],
        text: str,
        text_size: int,
        color: tuple[int, int, int],
    ):
        self.change_font_size(text_size)
        self.draw.text(pos, text, color, font = self.font)

    def draw_outlined_text(
        self,
        pos: tuple[int, int],
        text: str,
        text_size: int,
        color: tuple[int, int, int],
        outline_color: tuple[int, int, int],
        outline_size: int
    ):
        self.change_font_size(text_size)
        self.draw.text(pos, text, color, font = self.font, stroke_width = outline_size, stroke_fill = outline_color)
