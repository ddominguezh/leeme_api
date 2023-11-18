from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from leeme_app.main.app.word.application.use_case.filter.filter_by_characters_query import FilterByCharactersQuery, FilterByCharactersQueryHandler, FilterByCharactersQueryResponse
from leeme_app.main.app.word.domain.value_object.word import Word
from leeme_app.main.app.word.infrastructure.controller.words_response import WordsResponse
from leeme_app.main.app.word.infrastructure.repository.file_word_repository import FileWordRepository

from leeme_app.main.shared.domain.query_handler import QueryHandler

get_words_filter_by_characters_router = APIRouter()

async def _find_all_words_by_character_query_handler() -> QueryHandler:
    repository = FileWordRepository()
    return FilterByCharactersQueryHandler(repository)

@get_words_filter_by_characters_router.get("/api/v1/words/{mainCharacter}/{characters}", response_model=WordsResponse)
def get_words_filter_by_characters_controller(
    mainCharacter: str,
    characters: str,
    response: Response,
    handler: QueryHandler = Depends(_find_all_words_by_character_query_handler)
) -> WordsResponse:
    query = FilterByCharactersQuery(mainCharacter, characters.split(','))
    _filterResponse: FilterByCharactersQueryResponse = handler.process(query)
    response.status_code = status.HTTP_200_OK
    words = []
    for word in _filterResponse.words:
        words.append(word.value)
    return WordsResponse(**{"words": words})
    