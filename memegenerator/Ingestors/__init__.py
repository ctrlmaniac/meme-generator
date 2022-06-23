from .interface import IngestorInterface
from .text import TextIngestor
from .docx import DocxIngestor
from .csv import CSVIngestor

__all__ = [
    "IngestorInterface",
    "TextIngestor",
    "DocxIngestor",
    "CSVIngestor",
]
