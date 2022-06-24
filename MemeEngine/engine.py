"""MemeEngine class.

A class that generates meme
"""
import os
import random
import textwrap
import uuid
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Meme engine."""

    def __init__(self, output_dir: str):
        """Inizialize class.

        :param output_dir: a fully qualified path.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate meme.

        :param img_path: original image.
        :param text: the body of the quote.
        :param author: the author of the quote.
        :param width: the width of the meme image.

        Return the path of the generated meme.
        """
        BASE_DIR = Path(__file__).resolve().parent.parent
        TMP_DIR = os.path.join(BASE_DIR, self.output_dir)

        if not os.path.isdir(TMP_DIR):
            os.mkdir(TMP_DIR)

        temp_name = uuid.uuid4()

        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"{temp_name}.jpg")

        real_width, real_height = img.size
        height = int(real_height * width / real_width)
        img.thumbnail((width, height))

        text = textwrap.fill(text, width=40)
        draw = ImageDraw.Draw(img)

        count_line = 0
        for line in text.split("\n"):
            count_line += 1

        if count_line > 1:
            w, h = draw.textsize(text)
            text_position = (height - h) / 2
        else:
            text_position = random.choice(range(30, height - 100))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        # Fonts
        FONTS_DIR = os.path.join(BASE_DIR, "_data/Fonts")
        kalam = ImageFont.truetype(
            os.path.join(FONTS_DIR, "Kalam/Kalam-Bold.ttf"), 22
        )

        draw.text(
            (30, text_position),
            text,
            fill,
            kalam,
            stroke_width=1,
            stroke_fill=stroke_fill,
        )
        draw.text(
            (40, text_position + (count_line * 14) + 25),
            f"- {author}",
            fill,
            kalam,
            stroke_width=1,
            stroke_fill=stroke_fill,
        )

        img.save(outfile, "JPEG")

        return outfile
