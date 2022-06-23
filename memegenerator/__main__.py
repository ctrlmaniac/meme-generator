import os
from pathlib import Path
from .Ingestors import TextIngestor

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    txt = TextIngestor(
        os.path.join(BASE_DIR, "_data/SimpleLines/SimpleLines.txt")
    )

    txt.parse()
