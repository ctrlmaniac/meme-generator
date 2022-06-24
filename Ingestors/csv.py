"""CSVIngestor.

An ingestor to parse, read and save quotes from csv files.
"""
from typing import List

from pandas import read_csv

from QuoteEngine import QuoteModel

from .interface import IngestorInterface
from exceptions import InvalidFile


class CSVIngestor(IngestorInterface):
    """CSVIngestor.

    An ingestor that parses CSV files.
    """

    @classmethod
    def parse(cls, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel."""
        quotes = list()

        if not cls.can_ingest(infile):
            raise InvalidFile("CSV")
        else:
            csv = read_csv(infile)

            for i, row in csv.iterrows():
                quote = QuoteModel(row.body, row.author)
                quotes.append(quote)

        return quotes
