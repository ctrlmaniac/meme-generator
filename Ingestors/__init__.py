"""This file will export all ingestors."""

from .interface import IngestorInterface
from .text import TextIngestor
from .docx import DocxIngestor
from .csv import CSVIngestor
from .ingestor import Ingestor
from .pdf import PDFIngestor

__all__ = [
    "IngestorInterface",
    "TextIngestor",
    "DocxIngestor",
    "CSVIngestor",
    "Ingestor",
    "PDFIngestor",
]
