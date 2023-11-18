from abc import ABC, abstractmethod

from leeme_app.main.shared.domain.command import Command

class CommandHandler(ABC):

    @abstractmethod
    def process(self, command: Command):
        pass