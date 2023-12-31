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

    def test_words_with_main_character(self):
        words = WordsFactory.create(['dactilograma', 'decárea', 'definitud', 'deflación']).containsMainCharacter('c').value
        assert len(words) == 3
        assert 'dactilograma' == words[0].value
        assert 'decárea' == words[1].value
        assert 'deflación' == words[2].value

    def test_filter_words(self):
        words = WordsFactory.create(['dactilograma', 'decárea', 'definitud', 'deflación']).containsOnlyCharacters(['a', 'á', 'e', 'i', 'u', 'd', 'c', 'r', 'f', 'n', 't']).value
        assert 'decárea' == words[0].value
        assert 'definitud' == words[1].value

    def test_remove_ilegal_words(self):
        words = WordsFactory.create(['círuela', 'dactilograma', 'decárea', 'caceria', 'deflación']).removeIlegalCharacters().value
        assert len(words) == 2
        assert 'dactilograma' == words[0].value
        assert 'decárea' == words[1].value

    def test_filter_words_of_file(self):
        with open('{}/data/d.txt'.format(pathlib.Path().absolute())) as f:
            words = WordsFactory.create(f.read().splitlines()).containsOnlyCharacters(['a', 'á', 'e', 'i', 'u', 'd', 'c', 'r', 'f', 'n', 't']).value
            assert len(words) > 0

        