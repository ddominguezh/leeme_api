import pytest

from leeme_load.main.app.text.domain.text import Text, TextFactory

class TestWords:

    def test_create_text(self) -> None:
        text = TextFactory.create('Hola Alberto como estas')
        assert 'Hola Alberto como estas' == text.value

    def test_remove_number_of_text(self) -> None:
        text = TextFactory.create('Hola Alberto9 como estas')
        assert 'Hola Alberto como estas' == text.clean().value

    def test_remove_simbols_of_text(self) -> None:
        text = TextFactory.create('Hola Alberto, ¿como estas?')
        assert 'Hola Alberto como estas' == text.clean().value

    def test_remove_repeat_white_space_of_text(self) -> None:
        text = TextFactory.create('Hola  Alberto,   ¿como estas?')
        assert 'Hola Alberto como estas' == text.clean().value

    def test_remove_lines_text(self) -> None:
        text = TextFactory.create('Hola Alberto\ncomo estas')
        assert 'Hola Alberto como estas' == text.clean().value