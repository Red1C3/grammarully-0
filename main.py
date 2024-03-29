#!./.venv/bin/python

import curses
import sys

from language.sentence import Sentence
from grammar.rule import Rule
from grammar.checker import Checker
from test.tests import run_tests
from processor.window import Window
from processor.tk_window import TkWindow
def main():
    run_tests()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'editor':
            curses.wrapper(Window().loop)
        elif sys.argv[1] == 'tk':
            TkWindow()
    else:
        main()
