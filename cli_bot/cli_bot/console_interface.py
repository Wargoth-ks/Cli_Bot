from abc_interfaces import UserInterface
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style


class ConsoleInterface(UserInterface):
    def __init__(self, completer, complete_while_typing):
        self.history = InMemoryHistory()
        self.completer = completer
        self.complete_while_typing = complete_while_typing
        self.style = Style.from_dict({
            'completion-menu.completion': 'bg:#008888 #ffffff',
            'completion-menu.completion.current': 'bg:#00aaaa #000000',
            'scrollbar.background': 'bg:#88aaaa',
            'scrollbar.button': 'bg:#222222',
        })

    def get_user_input(self) -> str:
        return prompt(
            "\nEnter command: ",
            history=self.history,
            completer=self.completer,
            complete_while_typing=self.complete_while_typing,
            style=self.style
        )

    def display_output(self, output: str):
        print(output)
