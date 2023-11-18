from abc import ABC, abstractmethod

from leeme_app.main.shared.domain.query import Query
from leeme_app.main.shared.domain.query_response import QueryResponse

class QueryHandler(ABC):

    @abstractmethod
    def process(self, query: Query) -> QueryResponse:
        pass