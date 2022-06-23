"""Ingestor Interface.

An interface for ingesting quotes in different formats
"""
from abc import ABC, abstractmethod
from typing import List
from memegenerator.QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface.

    An abstract class for parsing quotes in different format files.
    """

    @abstractmethod
    def parse(self, infile: str) -> List[QuoteModel]:
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
        ingestor = cls(infile)

        return True if ingestor.accepts == extension else False
