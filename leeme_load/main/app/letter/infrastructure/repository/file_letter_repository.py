import pathlib

from leeme_load.main.app.letter.domain.value_object.letter import Letter
from leeme_load.main.app.letter.domain.repository.letter_repository import LetterRepository

class FileLetterRepository(LetterRepository):
    def save(self, letter: Letter) -> None:
        try:
            filePath = '{}/data/{}.txt'.format(pathlib.Path().absolute(), letter.value)
            oldWords = []
            with open(filePath) as f:
                oldWords = oldWords + f.read().lower().splitlines()
                f.close()
                
            with open(filePath, 'a') as f:
                for word in letter.words:
                    if word.lower() not in oldWords:
                        f.write('\n{}'.format(word))
                f.close()
        except:
            raise