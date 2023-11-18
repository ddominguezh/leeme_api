from dataclasses import dataclass

from leeme_app.main.app.word.domain.value_object.word import Word, WordFactory

@dataclass
class Words:
    value: [Word]

    def containsOnlyCharacters(self, characters: []) -> [Word]:
        withoutCharacters = []
        for word in self.value:
            if word.containsOnlyCharacters(characters):
                withoutCharacters.append(word)
        return withoutCharacters
    
class WordsFactory:

    @staticmethod
    def create(value: [str]) -> Words:
        return Words(list(map(WordFactory.create, value)))