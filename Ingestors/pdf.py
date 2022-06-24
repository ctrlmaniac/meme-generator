"""PDFIngestor.

Ingestor that parse and read PDF files.
"""
import os
import subprocess
import uuid
from pathlib import Path
from typing import List

from QuoteEngine import QuoteModel

from .interface import IngestorInterface
from .text import TextIngestor


class PDFIngestor(IngestorInterface):
    """TextIngestor.

    An ingestor that parses pdf files.
    """

    @classmethod
    def parse(cls, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel."""
        quotes = list()

        if not cls.can_ingest(infile):
            raise ValueError(
                "Unable to ingest file. Please, provide a PDF file."
            )
        else:
            BASE_DIR = Path(__file__).resolve().parent.parent
            pdftotext_bin = os.path.join(BASE_DIR, "pdftotext")

            tmp_dir = os.path.join(BASE_DIR, "tmp")
            tmp_file = os.path.join(tmp_dir, f"{uuid.uuid4()}.txt")
            if not os.path.isdir(tmp_dir):
                os.mkdir(tmp_dir)

            with open(tmp_file, "w") as file:
                file.write("")

            cmd = f"{pdftotext_bin} -layout -nopgbrk {infile} {tmp_file}"

            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)

            quotes = TextIngestor.parse(tmp_file)

            os.remove(tmp_file)

        return quotes
