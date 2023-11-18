import pytest

from leeme_app.main.app.word.domain.value_object.word import WordFactory

class TestWord:

    def test_create_word(self) -> None:
        word = WordFactory.create("hola")
        assert "hola" == word.value

    def test_create_word_with_comma(self) -> None:
        word = WordFactory.create("azulejero, ra")
        assert "azulejero" == word.value

    def test_contains_more_characters_than_necessary(self):
        word = WordFactory.create("gabarrero")
        assert False == word.containsOnlyCharacters(['a', 'e', 'i', 'o', 'u', 'g', 'r'])

    def test_contains_only_the_expected_characters(self):
        word = WordFactory.create("gabarrero")
        assert True == word.containsOnlyCharacters(['a', 'e', 'i', 'o', 'u', 'g', 'r', 'b'])