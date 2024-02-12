# grammarully-0
A rule-based grammar correction system.

## Usage
For the Tk interface run:
```./main.py tk```

For the ncurses interface (TUI) run:
```./main.py editor [input_file] [output_file]```

Note that the TUI interface will overwrite the `input_file` when no `output_file` was provided without prompt.

To run all the tests run: ```./main.py```

## Rules-Set
Most of the rules were inspired by [Daniel Naber work](https://www.danielnaber.de/languagetool/download/style_and_grammar_checker.pdf), while the rest are guessed manually by the team.

## POS Tag-Set
The project uses C5 tag-set, it guesses first the tags using PennTreebank set and converts them to C5 using a conversion map and  apply dictionary lookup afterwards.

## Troubleshoot
If you're using a recent Python version, `pattern` library will not work as it is in PyPI, you can either [patch it manually](https://github.com/piskvorky/gensim/issues/2438#issuecomment-644753776) or install a [patched version](https://github.com/i-be-snek/pattern-StopIteration-fix) instead.

## License
[GPL-3.0-or-later](./LICENSE)