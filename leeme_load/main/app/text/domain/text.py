from dataclasses import dataclass

@dataclass
class Text:
    _CHARACTERS = 'aáäbcdeéëfghiíïjklmnñoóöpqrstuúüvwxyz '
    value: str

    def clean(self):
        textCleaned = ''
        for character in list(self._change_line_to_whitespace()):
            if character.lower() in self._CHARACTERS and not(character == ' ' and textCleaned[-1::] == ' '):
                textCleaned = textCleaned + character
        return TextFactory.create(textCleaned)

    def _change_line_to_whitespace(self):
        return self.value.replace('\n', ' ')

class TextFactory:

    @staticmethod
    def create(value: str) -> Text:
        return Text(value)