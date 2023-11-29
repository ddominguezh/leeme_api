from leeme_load.main.app.word.domain.words import Words, WordsFactory

class StrToWords:

    def process(self, text: str) -> Words:
        return WordsFactory.create(text.split(' ')).clean().sorted()