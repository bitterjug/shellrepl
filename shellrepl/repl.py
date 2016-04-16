from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory


def main():
    history = InMemoryHistory()

    while True:
        text = prompt("$ ", history=history)
        print("you entered:", text)
    print("done")

if __name__ == "__main__":
    main()
