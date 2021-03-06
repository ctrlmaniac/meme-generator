"""Ingestor.

A Class that manages all ingestors.
"""
from .csv import CSVIngestor
from .docx import DocxIngestor
from .pdf import PDFIngestor
from .text import TextIngestor


class Ingestor:
    """Ingestor.

    A class that manages all ingestors
    """

    @classmethod
    def parse(cls, infile: str):
        """Parse a file.

        pass the file to the right ingestor.

        :param infile: a fully qualified path to the infile.
        """
        ext = infile.split(".")[-1].lower()

        if ext == "csv":
            return CSVIngestor.parse(infile)
        elif ext == "docx":
            return DocxIngestor.parse(infile)
        elif ext == "txt":
            return TextIngestor.parse(infile)
        elif ext == "pdf":
            return PDFIngestor.parse(infile)
        else:
            raise ValueError(
                "Invalid file! Please, provide a txt, docx, csv or pdf file!"
            )
