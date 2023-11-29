import pytest
from unittest.mock import Mock

from leeme_load.main.app.text.application.use_case.file_to_text import FileToText
from leeme_load.main.app.text.domain.repository.text_repository import TextRepository
from leeme_load.main.app.text.domain.text import TextFactory

class TestFileToText:

    def test_get_text(self) -> None:
        text = TextFactory.create('uno dos')
        repository = Mock(spec=TextRepository)
        repository.get.return_value = text
        useCase = FileToText(repository)
        response = useCase.process('example.txt')
        assert text.value == "uno dos"