from leeme_load.main.app.word.infrastructure.controller.get_words_controller import GetWordsController

class TestGetWordsController:

    def test_get_words_from_str(self) -> None:
        words = GetWordsController().get('uno dos tres')
        assert ['dos', 'tres', 'uno'] == words