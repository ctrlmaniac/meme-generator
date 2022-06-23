"""Ingestor Interface.

An interface for ingesting quotes in different formats
"""
from abc import ABC, abstractmethod
from typing import List
from memegenerator.QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface.
    An abstract class for parsing quotes in different format files
    """

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file and return a list of quotes
        :param path: a fully qualified pathname to a file

        Returns a List of quotes
        """
        pass

    @classmethod
    def can_ingest(cls, infile: str) -> bool:
        pass
