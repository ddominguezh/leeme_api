from leeme_load.main.app.text.domain.text import Text
from leeme_load.main.app.text.infrastructure.repository.file_text_repository import FileTextRepository
from leeme_load.main.app.text.application.use_case.file_to_text import FileToText

class GetTextFileController:

    def __init__(self):
        self.useCase = FileToText(FileTextRepository())

    def get(self, name: str) -> str:
        return self.useCase.process(name).value