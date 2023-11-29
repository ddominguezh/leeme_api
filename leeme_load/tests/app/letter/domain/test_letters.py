import pytest

from leeme_load.main.app.letter.domain.letters import Letters, LettersFactory

class TestLetters:

    def test_create_letters(self):
        letters = LettersFactory.create(['Alberto', 'como', 'cuando', 'estas', 'Hola', 'puedas', 'te', 'veo'])
        assert len(letters.value) == 7
        assert letters.value[0] == 'a'
        assert letters.value[0].words == ['Alberto']

        assert letters.value[1] == 'c'
        assert letters.value[1].words == ['como', 'cuando']

        assert letters.value[2] == 'e'
        assert letters.value[2].words == ['estas']

        assert letters.value[3] == 'h'
        assert letters.value[3].words == ['Hola']

        assert letters.value[4] == 'p'
        assert letters.value[4].words == ['puedas']

        assert letters.value[5] == 't'
        assert letters.value[5].words == ['te']

        assert letters.value[6] == 'v'
        assert letters.value[6].words == ['veo']