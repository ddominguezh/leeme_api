
from leeme_load.main.app.text.infrastructure.controller.get_text_file_controller import GetTextFileController
from leeme_load.main.app.word.infrastructure.controller.get_words_controller import GetWordsController
from leeme_load.main.app.letter.infrastructure.controller.save_letters_controller import SaveLettersController

class TestMain:

    def test_save_book(self) -> None:
        text = GetTextFileController().get('tortuga_y_liebre.txt')
        words = GetWordsController().get(text)
        SaveLettersController().save(words)