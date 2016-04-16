import os
from pathlib import Path
import itertools


def all_commands():
    """
    Returns a list of the commands in current $PATH
    """
    return itertools.chain.from_iterable(
        executables(path)
        for path in os.environ['PATH'].split(':')
    )


def executables(path):
    return (
        file.name for file in Path(path).iterdir()
        if os.access(str(file), os.X_OK)
    )
