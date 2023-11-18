from dataclasses import dataclass

@dataclass
class Word:
    value: str

    def containsOnlyCharacters(self, characters: []) -> bool:
        withoutCharacters = ""
        for character in set(self.value.lower()):
            if character not in characters:
                withoutCharacters = withoutCharacters + character
        return withoutCharacters == ""
    
class WordFactory:

    @staticmethod
    def create(value: str) -> Word:
        if(', ' in value):
            index = value.index(', ')
            return Word(value[:index])
        return Word(value)