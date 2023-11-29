from dataclasses import dataclass

from leeme_load.main.app.letter.domain.value_object.letter import Letter, LetterFactory

@dataclass
class Letters:
    _CHARACTERS = list('abcdefghijklmnñopqrstuvwxyz')
    value: [Letter]

    def __init__(self, value: [str]):
        self.value = []
        for character in self._CHARACTERS:
            letter = LetterFactory.create(character)
            for word in value:
                if word[0:1:].lower() == character:
                    letter = letter.add(word)
                    continue
                if not(letter.empty()):
                    break
            if not(letter.empty()):
                self.value.append(letter)
        


class LettersFactory:

    @staticmethod
    def create(value: [str]) -> Letters:
        return Letters(value)