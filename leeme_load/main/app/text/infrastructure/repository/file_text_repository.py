import pathlib

from leeme_load.main.app.text.domain.text import Text, TextFactory
from leeme_load.main.app.text.domain.repository.text_repository import TextRepository

class FileTextRepository(TextRepository):
    def get(self, name) -> Text:
        try:
            with open('{}/files/{}'.format(pathlib.Path().absolute(), name)) as f:
                return TextFactory.create(f.read())
        except:
            pass