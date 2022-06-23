import os
from pathlib import Path
from .Ingestors import DocxIngestor

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    quotes = DocxIngestor(
        os.path.join(BASE_DIR, "_data/SimpleLines/SimpleLines.docx")
    )

    quotes.parse()
