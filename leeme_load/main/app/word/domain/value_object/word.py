from dataclasses import dataclass

@dataclass
class Word:
    value: str

    def __hash__(self):
        return hash(self.value.lower())

    def __eq__(self, other):
        if isinstance(other, Word):
            return self.value.lower() == other.value.lower()
        if isinstance(other, str):
            return self.value.lower() == other.lower()
        return False

    def compare(self, other):
        if self.value.lower() < other.value.lower():
            return -1
        elif self.value.lower() > other.value.lower():
            return 1
        return 0

    def onlyCharacter(self):
        return len(self.value) <= 1
        
    @staticmethod
    def wordToStr(word) -> str:
        return word.value

class WordFactory:

    @staticmethod
    def create(value: str) -> Word:
        return Word(value)