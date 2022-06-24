"""DocxIngestor.

An ingestor to parse, read and save quotes from docx files.
"""
from typing import List

from docx import Document

from QuoteEngine import QuoteModel

from .interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """DocxIngestor.

    An ingestor that parses docx files.
    """

    @classmethod
    def parse(cls, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel."""
        quotes = list()

        if not cls.can_ingest(infile):
            print("Unable to ingest file. Please, provide a DOCX file.")
        else:
            doc = Document(infile)

            for para in doc.paragraphs:
                line = para.text
                line.strip()
                line = line.split(" - ")

                try:
                    quote = QuoteModel(line[0].strip('"'), line[1])
                    quotes.append(quote)
                except IndexError:
                    continue

        return quotes
