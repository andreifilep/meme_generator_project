"""Realize the IngestorInterface abstract base class and encapsulate helper classes"""
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .import_docx import DocxImporter
from .import_csv import CSVImporter
from .import_txt import TXTImporter
from .import_pdf import PDFImporter


class Ingestor(IngestorInterface):
    """Encapsulates quote ingestor classes for known file types."""
    importers = [DocxImporter, CSVImporter, TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest file with correct ingestor."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
