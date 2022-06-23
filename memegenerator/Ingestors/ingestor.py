"""Ingestor.
A Class that manages all ingestors.
"""
from .docx import DocxIngestor
from .text import TextIngestor
from .csv import CSVIngestor


class Ingestor:
    """Ingestor.
    A class that manages all ingestors"""

    @property
    def extension(self, infile):
        """Return the extension of the given infile.
        :param infile: a fully qualified path to the infile.
        """
        return infile.split(".")[-1].lower()

    def parse(self, infile: str):
        """Parse a file.
        pass the file to the right ingestor.
        :param infile: a fully qualified path to the infile.
        """
        ext = self.extension(infile)

        if ext == "csv":
            CSVIngestor.parse(infile)
        elif ext == "docx":
            DocxIngestor.parse(infile)
        elif ext == "txt":
            TextIngestor.pase(infile)
        else:
            raise ValueError(
                "Invalid file! Please, provide a txt, docx, csv or pdf file!"
            )
