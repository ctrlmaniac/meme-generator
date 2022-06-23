"""MemeGenerator class.

A class that generates meme
"""
import os
from random import random
import uuid
from PIL import Image, ImageFont, ImageDraw


class MemeGenerator:
    """MemeGenerator."""

    def __init__(self, output_dir: str):
        """Inizialize class.

        :param output_dir: a fully qualified path.
        """
        self.output = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate meme.

        :param img_path: original image.
        :param text: the body of the quote.
        :param author: the author of the quote.
        :param width: the width of the meme image.

        Return the path of the generated meme.
        """
        temp_name = uuid.uuid5()

        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"{temp_name}.jpg")

        real_width, real_height = img.size
        height = int(real_height * width / real_width)
        img.thumbnail((width, height))

        roboto_bold = ImageFont.truetype("../_data/Fonts/Roboto-Bold.ttf", 22)
        roboto_medium = ImageFont.truetype(
            "../_data/Fonts/Roboto-Medium.ttf", 18
        )

        text_position = random.choice(range(30, height - 50))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        draw = ImageDraw.Draw(img)
        draw.text(
            (30, text_position),
            text,
            fill,
            roboto_bold,
            stroke_width=1,
            stroke_fill=stroke_fill,
        )
        draw.text(
            (40, text_position + 25),
            f"- {author}",
            fill,
            roboto_medium,
            stroke_width=1,
            stroke_fill=stroke_fill,
        )

        img.save(outfile, "JPEG")

        return outfile
