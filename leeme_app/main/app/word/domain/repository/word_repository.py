from abc import ABC, abstractmethod
from typing import List

from leeme_app.main.app.word.domain.words import Words

class WordRepository(ABC):

    @abstractmethod
    def find_all(self, characters: [str]) -> Words:
        pass