import uuid
from leeme_app.main.app.word.domain.repository.word_repository import WordRepository
from leeme_app.main.app.word.domain.value_object.word import Word
from leeme_app.main.app.word.domain.words import Words

from leeme_app.main.shared.domain.query import Query
from leeme_app.main.shared.domain.query_handler import QueryHandler
from leeme_app.main.shared.domain.query_response import QueryResponse

class FilterByCharactersQuery(Query):
    def __init__(self, characters: []) -> None:
        super().__init__(uuid.uuid1())
        self.characters = characters

class FilterByCharactersQueryResponse(QueryResponse):
    def __init__(self, words: [Word]) -> None:
        self.words = words

class FilterByCharactersQueryHandler(QueryHandler):
    def __init__(self, repository: WordRepository):
        self.repository = repository

    def process(self, query: FilterByCharactersQuery) -> "FilterByCharactersQueryResponse":
        words :Words = self.repository.find_all(query.characters)
        return FilterByCharactersQueryResponse(words.containsOnlyCharacters(query.characters))