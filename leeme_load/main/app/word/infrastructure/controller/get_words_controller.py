from leeme_load.main.app.word.application.use_case.str_to_words import StrToWords
from leeme_load.main.app.word.domain.value_object.word import Word

class GetWordsController:

    def get(self, text: str) -> [str]:
        return list(map(Word.wordToStr, StrToWords().process(text).value))