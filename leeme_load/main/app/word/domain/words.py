from dataclasses import dataclass
from functools import cmp_to_key

from leeme_load.main.app.word.domain.value_object.word import Word, WordFactory

@dataclass
class Words:
    value: [Word]

    def sorted(self):
        return WordsFactory.copy(sorted(self.value, key=cmp_to_key(lambda item1, item2: item1.compare(item2))))

    def clean(self):
        return WordsFactory.copy(list(set(self._wordsWithMoreThanOneCharacter())))
    
    def _wordsWithMoreThanOneCharacter(self):
        words = []
        for word in self.value:
            if not(word.onlyCharacter()):
                words.append(word)
        return words


class WordsFactory:

    @staticmethod
    def create(value: [str]) -> Words:
        return Words(list(map(WordFactory.create, value)))
    
    @staticmethod
    def copy(value: [Word]) -> Words:
        return Words(value)