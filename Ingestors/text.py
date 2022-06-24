"""TextIngestor.

An ingestor to parse, read and save quotes from txt files.
"""
from multiprocessing.sharedctypes import Value
from typing import List

from QuoteEngine import QuoteModel

from .interface import IngestorInterface
from exceptions import InvalidFile


class TextIngestor(IngestorInterface):
    """TextIngestor.

    An ingestor that parses txt files.
    """

    @classmethod
    def parse(cls, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel."""
        quotes = list()

        if not cls.can_ingest(infile):
            raise InvalidFile("PDF")
        else:
            with open(infile, "r") as file:
                contents = file.readlines()

            for line in contents:
                line = line.strip("\n")
                line = line.split(" - ")
                quotes.append(QuoteModel(line[0].strip('"'), line[1]))

        return quotes
