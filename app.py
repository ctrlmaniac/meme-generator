"""This module implements Flask to serve the meme-generator online."""
import os
import random
import uuid
from pathlib import Path

import requests
from flask import Flask, abort, render_template, request

from Ingestors import Ingestor
from meme import generate_meme
from MemeEngine import MemeEngine

ROOT_DIR = Path(__file__).resolve().parent
app = Flask(__name__)

meme = MemeEngine("./static")


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
    tmp_image = os.path.join(ROOT_DIR, f"tmp/{uuid.uuid4()}.jpg")
    if not os.path.isdir(os.path.join(ROOT_DIR, "tmp")):
        os.mkdir(os.path.join(ROOT_DIR, "tmp"))

    # Check if image url is valid
    try:
        image_url = request.form.get("image_url")
        img_data = requests.get(image_url, stream=True).content
    except (
        requests.exceptions.MissingSchema,
        requests.exceptions.ConnectionError,
    ):
        return "Please, provide a valid url"

    with open(tmp_image, "wb") as f:
        f.write(img_data)

    body = request.form.get("body", "")
    author = request.form.get("author", "")
    path = generate_meme(tmp_image, body, author)

    os.remove(tmp_image)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
