"""Ingestor Interface.

An interface for ingesting quotes in different formats
"""
from abc import ABC
from typing import List
from QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface.

    An abstract class for parsing quotes in different format files.
    """

    accepts = (
        "txt",
        "docx",
        "pdf",
        "csv",
    )

    @classmethod
    def parse(cls, infile: str) -> List[QuoteModel]:
        """Parse a file and return a list of quotes.

        :param infile: a fully qualified pathname to a file.

        Returns a List of quotes.
        """
        pass

    @classmethod
    def can_ingest(cls, infile) -> bool:
        """Check if the given infile is a txt file.

        Returns boolean.
        """
        extension = infile.split(".")[-1]

        return True if extension in cls.accepts else False
