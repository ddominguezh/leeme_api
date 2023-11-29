from leeme_load.main.app.letter.domain.letters import Letters, LettersFactory
from leeme_load.main.app.letter.domain.repository.letter_repository import LetterRepository

class SaveWords:
    
    def __init__(self, repository: LetterRepository):
        self.repository = repository

    def process(self, words: [str]) -> None:
        letters = LettersFactory.create(words)
        for letter in letters.value:
            self.repository.save(letter)