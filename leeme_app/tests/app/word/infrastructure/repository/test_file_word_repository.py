import pytest
import pathlib

from leeme_app.main.app.word.domain.words import WordsFactory
from leeme_app.main.app.word.infrastructure.repository.file_word_repository import FileWordRepository

class TestFileWordRepository:

    def test_get_words_with_characters(self):
        repository = FileWordRepository()
        words = repository.find_all('a')
        assert len(words.value) == 11135