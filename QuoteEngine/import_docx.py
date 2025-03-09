"""Import quotes from known file types."""

from typing import List
import docx
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class DocxImporter(IngestorInterface):
    """Imports quotes from docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of quotes from parsing docx files."""
        if not cls.can_ingest(path):
            raise ValueError(f'File type not supported for {path}')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(
                    parse[0].replace('"', ''),
                    parse[1].replace('"', ''))
                quotes.append(new_quote)

        return quotes
