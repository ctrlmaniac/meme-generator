"""This module implements Flask to serve the meme-generator online."""
from pathlib import Path
import random
import os
import requests
from flask import Flask, render_template, abort, request
from .MemeEngine import MemeEngine
from .Ingestors import Ingestor


app = Flask(__name__)

meme = MemeEngine("./static")

ROOT_DIR = Path(__file__).resolve().parent.parent


def setup():
    """Load all resources."""
    quote_files = [
        os.path.join(ROOT_DIR, "_data/DogQuotes/DogQuotesTXT.txt"),
        os.path.join(ROOT_DIR, "_data/DogQuotes/DogQuotesDOCX.docx"),
        os.path.join(ROOT_DIR, "_data/DogQuotes/DogQuotesPDF.pdf"),
        os.path.join(ROOT_DIR, "_data/DogQuotes/DogQuotesCSV.csv"),
    ]

    quotes = []
    for f in quote_files:
        parsed = Ingestor.parse(f)
        quotes.extend(parsed)

    images_path = os.path.join(ROOT_DIR, "_data/photos/dog/")

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
