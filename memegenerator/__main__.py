"""This file allows the use of the memegenerator module.

It is required if run the generator with the command python -m memegenerator.
"""
from argparse import ArgumentParser
from memegenerator.meme import generate_meme


parser = ArgumentParser(description="Generates meme and prints their path")
parser.add_argument(
    "--path",
    type=str,
    default=None,
    help="path to an image file",
)
parser.add_argument(
    "--body",
    type=str,
    default=None,
    help="quote body to add to the image",
)
parser.add_argument(
    "--author",
    type=str,
    default=None,
    help="quote author to add to the image",
)
args = parser.parse_args()

generate_meme(args.path, args.body, args.author)
