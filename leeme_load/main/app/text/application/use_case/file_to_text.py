from leeme_load.main.app.text.domain.text import Text
from leeme_load.main.app.text.domain.repository.text_repository import TextRepository

class FileToText:
    
    def __init__(self, repository: TextRepository):
        self.repository = repository

    def process(self, name) -> Text:
        return self.repository.get(name).clean()