from typing import List
from pydantic import BaseModel

from leeme_app.main.app.word.domain.value_object.word import Word

class WordsResponse(BaseModel):
    words: List[str]