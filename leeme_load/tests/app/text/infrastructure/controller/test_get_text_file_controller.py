import pytest

from leeme_load.main.app.text.domain.text import Text
from leeme_load.main.app.text.infrastructure.controller.get_text_file_controller import GetTextFileController

class TestGetTextFileController:

    def test_get_text_file(self) -> None:
        text = GetTextFileController().get('example.txt')
        assert 'hola Alberto como estas' == text