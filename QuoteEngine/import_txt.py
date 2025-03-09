from typing import List
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class TXTImporter(IngestorInterface):
    """Imports quotes from txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of quotes from parsing txt files."""
        if not cls.can_ingest(path):
            raise ValueError(f'File type not supported for {path}')

        quotes = []
        file = open(path, 'r', encoding='utf-8-sig')
        lines = file.readlines()

        for line in lines:
            if len(line) > 1:
                new_quote = QuoteModel(line.split('-')[0], line.split('-')[1])
                quotes.append(new_quote)

        return quotes
