"""TextIngestor.

An ingestor to parse, read and save quotes from txt files.
"""
from typing import List

from QuoteEngine import QuoteModel

from .interface import IngestorInterface


class TextIngestor(IngestorInterface):
    """TextIngestor.

    An ingestor that parses txt files.
    """

    @classmethod
    def parse(cls, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel."""
        quotes = list()

        if not cls.can_ingest(infile):
            print("Unable to ingest file. Please, provide a TXT file.")
        else:
            with open(infile, "r") as file:
                contents = file.readlines()

            for line in contents:
                line = line.strip("\n")
                line = line.split(" - ")
                quotes.append(QuoteModel(line[0].strip('"'), line[1]))

        return quotes
