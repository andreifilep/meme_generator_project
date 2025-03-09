from typing import List
from abc import ABC, abstractmethod
from .quote_model import QuoteModel
import re
'''Implement an abstract base class, IngestorInterface. This class should 
define two methods with the following class method signatures: 
def can_ingest(cls, path) -> boolean and 
def parse(cls, path: str) -> List[QuoteModel]'''


class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
