"""Import quotes from known file types."""

from typing import List
import pandas as pd
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class CSVImporter(IngestorInterface):
    """Imports quotes from csv files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of quotes from parsing csv files."""
        if not cls.can_ingest(path):
            raise ValueError(f'File type not supported for {path}')

        quotes = []
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
