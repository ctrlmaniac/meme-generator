import os
from pathlib import Path
from .Ingestors import CSVIngestor

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    quotes = CSVIngestor(
        os.path.join(BASE_DIR, "_data/SimpleLines/SimpleLines.csv")
    )

    quotes.parse()
