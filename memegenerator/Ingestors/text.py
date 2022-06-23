"""TextIngestor.

An ingestor to parse, read and save quotes from txt files.
"""
from typing import List

from ..QuoteEngine import QuoteModel
from .interface import IngestorInterface


class TextIngestor(IngestorInterface):
    def __init__(self, infile):
        self.accepts = "txt"
        self.infile = infile

    def parse(self) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel"""
        quotes = list()

        if not self.can_ingest(self.infile):
            print("Unable to ingest file. Please, provide a TXT file.")
        else:
            with open(self.infile, "r") as infile:
                contents = infile.readlines()

            for line in contents:
                line = line.strip("\n")
                line = line.split(" - ")
                quotes.append(QuoteModel(line[1], line[0].strip('"')))

        return quotes
