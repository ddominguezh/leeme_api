import pytest

from leeme_load.main.app.word.application.use_case.str_to_words import StrToWords
from leeme_load.main.app.word.domain.words import Words

class TestStrToWords:

    def test_get_words(self) -> None:
        useCase = StrToWords()
        response = useCase.process('uno dos')
        assert response.value == ['dos', 'uno']