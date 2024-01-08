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
                            self.buffer_cache, submit, add_space = self.buffer.write_char(
                                c)
                            if submit > 0:
                                if add_space:
                                    self.text += ' '
                                self.text += self.buffer_cache[:submit]
                                self.buffer_cache = ''
            except FileNotFoundError:
                pass

    def loop(self, w: window):
        self.w = w
        curses.start_color()
        curses.use_default_colors()
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
                self.buffer_cache, submit, add_space = self.buffer.write_char(chr(c))
                if submit > 0:
                    if add_space:
                        self.text += ' '
                    self.text += self.buffer_cache[:submit]
                    self.buffer_cache = ''
            if c == curses.KEY_BACKSPACE:
                if len(self.buffer_cache) > 0:
                    self.buffer_cache = self.buffer.pop_char()
                else:
                    self.text = self.text[:-1]
                    stop_token_index = -1
                    for t in Buffer.STOP_TOKENS:
                        try:
                            stop_token_index = max(stop_token_index, self.text.rindex(t))
                        except ValueError:
                            pass
                    if stop_token_index != -1:
                        self.buffer_cache = self.buffer.set_without_processing(self.text[stop_token_index + 1:])
                        self.text = self.text[:stop_token_index + 1]
            w.erase()
            w.addstr(self.text + self.buffer_cache)
            self.w.refresh()
