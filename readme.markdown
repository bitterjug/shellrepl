# Playing with the awesome Prompt Toolkit

Let's see what we can do based on [the
tutorial](https://github.com/jonathanslenders/python-prompt-toolkit/tree/master/examples/tutorial)
and the shell.

Amazingly easy to set up a command line with (some) colouring and some
completion

- [ ] Consider using `compgen` to generate the completion words instead of
  traversing `$PATH` myself (although that was fun)

- [x] Wire up a shell to process the input

- [ ] `word_completer` apparently treats '-' as a word separator so doesn't
  properly complete commands-like-this.
