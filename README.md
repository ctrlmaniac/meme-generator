# meme-generator

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A meme generator written in python and served as a command-line tool and with flask!

## Dependencies

You can check the dependencies list int the [pyproject.toml](./pyproject.toml) or in the [requirements.txt](requirements.txt)

You have to install **xpdf command-line tool**. Check out [here](https://www.xpdfreader.com/download.html) how to download and run xpdf.

For linux users: You don't have to install xpdf since it comes packaged with this repository!

Here's a dependecies list:

- python = "^3.8"
- python-docx = "^0.8.11"
- pandas = "^1.4.3"
- Pillow = "^9.1.1"
- requests = "^2.28.0"
- Flask = "^2.1.2"

### Poetry

If you use poetry just run `poetry install --no-dev` to install all dependencies.
A virtual environment will be created and all dependencies will be installed.

### Virtual Environment

To instantiate a virtual environment run the following commands:

`python3 -m venv .venv`

This will create a virtual environment in the **.venv** folder

Run `python3 ./venv/bin/activate` to activate the virtual environment.

Then run `pip install -r requirements.txt` to install all dependencies.

## How to run

You can either run the **meme-generator** via the command-line tool or by running flask.

### Command-line instructions

After installing and activate the virtual environment run the following command to generate a random meme:

```
python meme.py
```

You can pass the following argumets:

- path: a path to a file.
- body: the body of the quote.
- author: the author of the quote.

you can pass arguments with the double dash!

Example:

```
python meme.py --body "To be or not to be" --author Shakespeare
```

### Browser

After installing and activate the virtual environment run the following command to spawn a flask server:

```
python app.py
```

This will create a link that you can click to inspect the meme generator via browser!

## Modules

Here you will find a description of all modules in this repository along with a brief description.

### Ingestors

This module will ingest, open, read and parse multiple files of different type and will return a list of quotes contained in those files.

#### CSVIngestor

This class will open, reand and parse a CSV file. It uses **pandas** to parse a CSV file.
It will return a list of quotes contained in the CSV file.

#### DocxIngestor

This class will open, read and parse a DOCX file. It uses **python-docx** to parse the file into a list of quotes.

#### PDFIngestor

This class will open, read and parse a PDF file. it uses **xpdf** to parse the file into a txt temporary file.

#### TextIngestor

This class will open, read and parse a TXT file. It will return a list of quotes.

#### Ingestor

This class will check the file extension of the given file and will pass the file to the right ingestor.

#### IngestorInterface

This class is an interface that will act like a parent class for all ingestors sub-classes.

### MemeEngine

This class will take a path to where the meme will be saved as an argument when instantiated.
If you call `make_meme` method on this class by passing the source image, the body of the quote and the author,
it will generate a meme.

### QuoteEngine

This class will represent a Quote. A Quote must contain a body and an author.
