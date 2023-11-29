import pytest

from leeme_load.main.app.letter.domain.value_object.letter import Letter, LetterFactory

class TestLetter:

    def test_create_letter(self) -> None:
        letter = LetterFactory.create('a')
        assert 'a' == letter.value
        assert []  == letter.words

    def test_equals_letter(self) -> None:
        letter = LetterFactory.create('a')
        assert 'a' == letter

    def test_add_word_to_letter(self) -> None:
        letter = LetterFactory.create('a')
        assert 'a' == letter.value
        assert []  == letter.words
        letter = letter.add('ala')
        assert ['ala']  == letter.words

    def test_exception_invalid_add_word_to_letter(self) -> None:
        letter = LetterFactory.create('a')
        assert 'a' == letter.value
        assert []  == letter.words
        with pytest.raises(ValueError) as err:
            letter = letter.add('Pala')
        assert err.typename == 'ValueError'
        assert str(err.value) == 'The word Pala not start with a'

    def test_empty_letter(self) -> None:
        assert True == LetterFactory.create('a').empty()

    def test_not_empty_letter(self) -> None:
        letter = LetterFactory.create('a')
        letter = letter.add('ala')
        assert False == letter.empty()