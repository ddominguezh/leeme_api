import json
import pathlib

from leeme_app.main.app.word.domain.repository.word_repository import WordRepository
from leeme_app.main.app.word.domain.value_object.word import Word
from leeme_app.main.app.word.domain.words import Words, WordsFactory

class FileWordRepository(WordRepository):

    def find_all(self, characters: []) -> Words:
        words = []
        for character in characters:
            try:
                with open('{}/data/{}.txt'.format(pathlib.Path().absolute(), character)) as f:
                    words = words + f.read().splitlines()
            except:
                pass
        return WordsFactory.create(words)