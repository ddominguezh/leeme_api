from leeme_load.main.app.letter.application.use_case.save_words import SaveWords
from leeme_load.main.app.letter.infrastructure.repository.file_letter_repository import FileLetterRepository
class SaveLettersController:

    def __init__(self):
        self.useCase = SaveWords(FileLetterRepository())

    def save(self, words: [str]):
        self.useCase.process(words)