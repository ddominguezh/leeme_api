from abc import ABC, abstractmethod

from leeme_load.main.app.letter.domain.value_object.letter import Letter

class LetterRepository(ABC):

    @abstractmethod
    def save(self, letter: Letter) -> None:
        pass