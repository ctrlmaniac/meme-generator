"""PDFIngestor.

Ingestor that parse and read PDF files.
"""
import subprocess
import os
from pathlib import Path
from typing import List
import uuid

from .text import TextIngestor

from QuoteEngine import QuoteModel
from .interface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """TextIngestor.

    An ingestor that parses txt files.
    """

    @classmethod
    def parse(cls, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel."""
        quotes = list()

        BASE_DIR = Path(__file__).resolve().parent.parent
        pdftotext_bin = os.path.join(BASE_DIR, "pdftotext")

        tmp_dir = os.path.join(BASE_DIR, "tmp")
        tmp_file = os.path.join(tmp_dir, f"{uuid.uuid4()}.txt")
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)

        cmd = f"{pdftotext_bin} -layout -nopgbrk {infile} {tmp_file}"

        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)

        quotes = TextIngestor.parse(tmp_file)

        os.remove(tmp_file)

        return quotes