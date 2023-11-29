from dataclasses import dataclass

@dataclass
class Letter:
    value: str
    words: [str]

    def __eq__(self, other):
        if isinstance(other, Letter):
            return self.value.lower() == other.value.lower()
        if isinstance(other, str):
            return self.value.lower() == other.lower()
        return False

    def add(self, word: str):
        if self.value.lower() == word[0:1:].lower():
            return LetterFactory.copy(self.value, self.words + [word])
        raise ValueError('The word ' + word + ' not start with ' + self.value)

    def empty(self) -> bool:
        return len(self.words) == 0


class LetterFactory:

    @staticmethod
    def create(value: str) -> Letter:
        return Letter(value, [])

    @staticmethod
    def copy(value: str,  words: [str]) -> Letter:
        return Letter(value, words)