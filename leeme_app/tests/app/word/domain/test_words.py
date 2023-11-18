import pytest
import pathlib

from leeme_app.main.app.word.domain.words import WordsFactory

class TestWords:

    def test_create_words(self):
        words = WordsFactory.create(['dactilograma', 'decárea', 'definitud', 'deflación'])
        assert 'dactilograma' == words.value[0].value
        assert 'decárea' == words.value[1].value
        assert 'definitud' == words.value[2].value
        assert 'deflación' == words.value[3].value

    def test_filter_words(self):
        words = WordsFactory.create(['dactilograma', 'decárea', 'definitud', 'deflación']).containsOnlyCharacters(['a', 'á', 'e', 'i', 'u', 'd', 'c', 'r', 'f', 'n', 't'])
        assert 'decárea' == words[0].value
        assert 'definitud' == words[1].value

    def test_filter_words_of_file(self):
        with open('{}/data/d.txt'.format(pathlib.Path().absolute())) as f:
            words = WordsFactory.create(f.read().splitlines()).containsOnlyCharacters(['a', 'á', 'e', 'i', 'u', 'd', 'c', 'r', 'f', 'n', 't'])
            assert len(words) > 0

        