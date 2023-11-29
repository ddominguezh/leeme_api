import pytest

from leeme_load.main.app.word.domain.words import Words, WordsFactory

class TestWords:

    def test_create_words(self) -> None:
        words = WordsFactory.create(['Hola', 'Alberto', 'como', 'estas'])
        assert ['Hola', 'Alberto', 'como', 'estas'] == words.value

    def test_sorted_words(self) -> None:
        words = WordsFactory.create(['Hola', 'Alberto', 'como', 'estas']).sorted()
        assert ['Alberto', 'como', 'estas', 'Hola'] == words.value

    def test_clean_words(self) -> None:
        words = WordsFactory.create(['Hola', 'Alberto', 'como', 'estas', 'Alberto']).clean().sorted()
        assert ['Alberto', 'como', 'estas', 'Hola'] == words.value

    def test_clean_ignore_case_words(self) -> None:
        words = WordsFactory.create(['Hola', 'Alberto', 'como', 'estas', 'aLBERTO']).clean().sorted()
        assert ['Alberto', 'como', 'estas', 'Hola'] == words.value