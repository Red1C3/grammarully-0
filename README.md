# grammarly-0
A rule-based grammar correction system.

## Usage
For the Tk interface run:
```./main.py tk```

For the ncurses interface (TUI) run:
```./main.py editor [input_file] [output_file]```

Note that the TUI interface will overwrite the `input_file` when no `output_file` was provided without prompt.

To run all the tests run: ```./main.py```

## POS Tag-Set
The project uses C5 tag-set, it guesses first the tags using PennTreebank set and converts them to C5 using a conversion map and dictionary lookup.

## License
[GPL-3.0-or-later](./LICENSE)