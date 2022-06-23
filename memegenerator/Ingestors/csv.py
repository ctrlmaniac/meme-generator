"""CSVIngestor.

An ingestor to parse, read and save quotes from csv files.
"""
from typing import List

from pandas import read_csv

from ..QuoteEngine import QuoteModel
from .interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    def __init__(self):
        self.accepts = "csv"

    def parse(self, infile) -> List[QuoteModel]:
        """Parse the infile and return a list of QuoteModel"""
        quotes = list()

        if not self.can_ingest(infile):
            print("Unable to ingest file. Please, provide a CSV file.")
        else:
            csv = read_csv(infile)

            for i, row in csv.iterrows():
                quote = QuoteModel(row.author, row.body)
                quotes.append(quote)

        return quotes
