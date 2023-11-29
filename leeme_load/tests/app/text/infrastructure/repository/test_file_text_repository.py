import pytest

from leeme_load.main.app.text.domain.text import Text
from leeme_load.main.app.text.infrastructure.repository.file_text_repository import FileTextRepository

class TestFileTextRepository:

    def test_load_file(self):
        repository = FileTextRepository()
        text = repository.get('example.txt')
        assert 'hola Alberto como estas' == text.clean().value