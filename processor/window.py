import curses
import time
from curses import window, setsyx
from curses.ascii import isalnum, ispunct, isspace
from processor.buffer import Buffer


class Window:
    def __init__(self):
        self.w = None
        self.text = ''
        self.buffer = Buffer()
        self.buffer_cache = ''

    def loop(self, w: window):
        self.w = w
        while True:
            c = w.getch()
            if isalnum(c) or ispunct(c) or isspace(c):
                self.buffer_cache, submit = self.buffer.write_char(chr(c))
                if submit > 0:
                    self.text += self.buffer_cache[:submit]
                    self.buffer_cache = ''
            w.erase()
            w.addstr(self.text + self.buffer_cache)
            self.w.refresh()
