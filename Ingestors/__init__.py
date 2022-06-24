"""This file will export all ingestors."""

from .csv import CSVIngestor
from .docx import DocxIngestor
from .ingestor import Ingestor
from .interface import IngestorInterface
from .pdf import PDFIngestor
from .text import TextIngestor

__all__ = [
    "IngestorInterface",
    "TextIngestor",
    "DocxIngestor",
    "CSVIngestor",
    "Ingestor",
    "PDFIngestor",
]
