import pytest
import pathlib

from leeme_load.main.app.letter.domain.value_object.letter import Letter, LetterFactory
from leeme_load.main.app.letter.infrastructure.repository.file_letter_repository import FileLetterRepository

class TestFileLetterRepository:

    def test_save_words_in_file(self) -> None:
        letter = LetterFactory.create('_').add('_uno').add('_dos').add('_tres')
        FileLetterRepository().save(letter)