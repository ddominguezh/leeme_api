import pytest
from unittest.mock import Mock
from leeme_app.main.app.word.application.use_case.filter.filter_by_characters_query import FilterByCharactersQuery, FilterByCharactersQueryHandler

from leeme_app.main.app.word.domain.repository.word_repository import WordRepository
from leeme_app.main.app.word.domain.words import WordsFactory

class TestFilterByCharactersQuery:

    def test_filter_words(self) -> None:
        words = WordsFactory.create(['uno', 'dos'])
        repository = Mock(spec=WordRepository)
        repository.find_all.return_value = words
        useCase = FilterByCharactersQueryHandler(repository)
        response = useCase.process(FilterByCharactersQuery('u', ['u', 'n', 'o', 'd']))
        assert len(response.words) == 1
        assert response.words[0].value == "uno"