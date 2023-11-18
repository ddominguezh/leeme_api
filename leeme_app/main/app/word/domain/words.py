from dataclasses import dataclass

from leeme_app.main.app.word.domain.value_object.word import Word, WordFactory

@dataclass
class Words:
    value: [Word]

    def containsOnlyCharacters(self, characters: []):
        withoutCharacters = []
        for word in self.value:
            if word.containsOnlyCharacters(characters):
                withoutCharacters.append(word)
        return WordsFactory.copy(withoutCharacters)
    
    def removeIlegalCharacters(self):
        withoutIlegalWords = []
        ilegalsWords = ['ce', 'ci', 'cé', 'cí']
        for word in self.value:
            isIlegalWord = False
            for ilegalWord in ilegalsWords:
                if ilegalWord in word.value:
                    isIlegalWord = True
                    break
            if isIlegalWord == False:
                withoutIlegalWords.append(word)
        return WordsFactory.copy(withoutIlegalWords)

class WordsFactory:

    @staticmethod
    def create(value: [str]) -> Words:
        return Words(list(map(WordFactory.create, value)))
    
    @staticmethod
    def copy(value: [Word]) -> Words:
        return Words(value)