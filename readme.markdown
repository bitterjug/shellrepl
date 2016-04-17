# Playing with the awesome Prompt Toolkit

Let's see what we can do based on [the
tutorial](https://github.com/jonathanslenders/python-prompt-toolkit/tree/master/examples/tutorial)
and the shell.

Amazingly easy to set up a command line with (some) colouring and some
completion

- [ ] Consider using `compgen` to generate the completion words instead of
  traversing `$PATH` myself (although that was fun)

- [ ] Wire up a shell to process the input

- [ ] `word_completer` apparently treats '-' as a word separator so doesn't
  properly complete commands-like-this.

Here's how to use pexpect to wrap a bash repl to use as the back-end:

         from pexpect.replwrap import bash 
         x=bash()                   
         x.child.logfile = sys.stdout
         x.run_command("ls /bin")   
         s=x.run_command("ls /bin")  
