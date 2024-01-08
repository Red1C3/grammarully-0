import curses
import time
from curses import window, setsyx
from curses.ascii import isalnum, ispunct, isspace
from processor.buffer import Buffer
from sys import argv


class Window:
    def __init__(self):
        self.w = None
        self.text = ''
        self.buffer = Buffer()
        self.buffer_cache = ''
        if len(argv) > 2:
            self.filepath = argv[2]
            try:
                with open(argv[2]) as txt_file:
                    for line in txt_file:
                        for c in line:
                            self.buffer_cache, submit = self.buffer.write_char(
                                c)
                            if submit > 0:
                                self.text += self.buffer_cache[:submit]
                                self.buffer_cache = ''
            except FileNotFoundError:
                pass

    def loop(self, w: window):
        self.w = w
        self.w.addstr(self.text)
        while True:
            try:
                c = w.getch()
            except KeyboardInterrupt:
                if len(argv) > 2:
                    if len(argv) > 3:
                        self.filepath = argv[3]
                    f = open(self.filepath, 'w')
                    f.write(self.text+self.buffer_cache)
                    f.close()
                return
            if isalnum(c) or ispunct(c) or isspace(c):
                self.buffer_cache, submit = self.buffer.write_char(chr(c))
                if submit > 0:
                    self.text += self.buffer_cache[:submit]
                    self.buffer_cache = ''
            w.erase()
            w.addstr(self.text + self.buffer_cache)
            self.w.refresh()
