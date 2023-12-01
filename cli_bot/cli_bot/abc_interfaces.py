from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def get_user_input(self) -> str:
        pass

    @abstractmethod
    def display_output(self, output: str):
        pass