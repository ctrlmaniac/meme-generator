"""DocxIngestor.

An ingestor to parse, read and save quotes from docx files.
"""
from docx import Document
from typing import List

from ..QuoteEngine import QuoteModel
from .interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    def __init__(self):
        self.accepts = "docx"

    def parse(self, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel"""
        quotes = list()

        if not self.can_ingest(infile):
            print("Unable to ingest file. Please, provide a DOCX file.")
        else:
            doc = Document(infile)

            for para in doc.paragraphs:
                line = para.text
                line.strip()
                line = line.split(" - ")

                try:
                    quote = QuoteModel(line[1], line[0].strip('"'))
                    quotes.append(quote)
                except IndexError:
                    continue

        return quotes
