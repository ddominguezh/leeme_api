from abc import ABC, abstractmethod
from typing import List

from leeme_load.main.app.text.domain.text import Text

class TextRepository(ABC):

    @abstractmethod
    def get(self, name) -> Text:
        pass