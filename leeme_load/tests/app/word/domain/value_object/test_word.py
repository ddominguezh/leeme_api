import pytest

from leeme_load.main.app.word.domain.value_object.word import WordFactory

class TestWord:

    def test_create_word(self) -> None:
        word = WordFactory.create("hola")
        assert "hola" == word.value

    def test_words_equals(self) -> None:
        assert WordFactory.create("hola") == WordFactory.create("HoLa")

    def test_words_equals_str(self) -> None:
        assert WordFactory.create("hola") == "HoLa"