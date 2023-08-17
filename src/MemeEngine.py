"""Meme Engine model."""

import random
import Exceptions
import textwrap
from Exceptions import ExceptionFilePath
from Exceptions import exception
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """Meme Engine."""

    def __init__(self, path):
        """Init path file."""
        self.temp_dir = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Gernerate meme."""
        path_img = f"{self.temp_dir}/{random.randint(0,1000000)}.png"

        if width >= 500:
            width = 500
        try:
            with Image.open(img_path) as img:
                ratio_img = img.height / img.width
                height = width * ratio_img
                img = img.resize((int(width), int(height)))
                fsize = int(img.height / 20)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("./_data/arial.ttf", fsize)

                xl = random.randint(0, int(img.width / 4))
                yl = random.randint(0, int(img.height - fsize * 4))

                wrapper = textwrap.TextWrapper(width=40)
                word_list = wrapper.wrap(text=text)
                line_text = "\n".join(item.center(40) for item in word_list)

                draw.text((xl, yl), line_text, font=font, fill=(0, 0, 0))
                draw.text((int(xl * 1.5), (yl * 1.5)), " - " + author, 
                font=font)

                img.save(path_img)
        except Exception:
            raise ExceptionFilePath("Invalid path")
        return path_img
