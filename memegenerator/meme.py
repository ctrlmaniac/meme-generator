"""A command-line tool for generating modules."""

from argparse import ArgumentParser
import os
from pathlib import Path
import random

from .MemeEngine import MemeEngine
from .QuoteEngine import QuoteModel
from .Ingestors import Ingestor


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None
    BASE_DIR = Path(__file__).resolve().parent

    if path is None:
        images = os.path.join(BASE_DIR, "_data/photos/dog/")
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            os.path.join(BASE_DIR, "_data/DogQuotes/DogQuotesTXT.txt"),
            os.path.join(BASE_DIR, "_data/DogQuotes/DogQuotesDOCX.docx"),
            os.path.join(BASE_DIR, "_data/DogQuotes/DogQuotesPDF.pdf"),
            os.path.join(BASE_DIR, "_data/DogQuotes/DogQuotesCSV.csv"),
        ]
        quotes = []
        for f in quote_files:
            parsed = Ingestor.parse(f)
            quotes.extend(parsed)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    print(quote)

    meme = MemeEngine("tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = ArgumentParser(description="Generates meme and prints their path")
    parser.add_argument(
        "--path",
        type=str,
        help="path to an image file",
    )
    parser.add_argument(
        "--body",
        type=str,
        help="quote body to add to the image",
    )
    parser.add_argument(
        "--author",
        type=str,
        help="quote author to add to the image",
    )
    args = parser.parse_args()
    generate_meme(args.path, args.body, args.author)
