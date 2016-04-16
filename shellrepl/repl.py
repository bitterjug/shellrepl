from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

from pygments.lexers.shell import BashLexer

from .commands import all_commands


command_completer = WordCompleter(all_commands())


def main():
    history = InMemoryHistory()

    while True:
        text = prompt(
            "$ ",
            history=history,
            lexer=BashLexer,
            completer=command_completer
        )
        print("you entered:", text)
    print("done")
