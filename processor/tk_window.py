from tkinter import *
from processor.buffer import Buffer


class TkWindow:
    def __init__(self):
        self.text = ''
        self.buffer = Buffer()
        self.buffer_cache = ''

        self.root = Tk()
        self.root.geometry('400x300')
        self.root.title('grammarly-0')
        self.sv = StringVar()
        self.text_box = Text(self.root)
        self.text_box.bind('<KeyRelease>', self.on_key_release)
        self.text_box.pack(expand=True)
        self.root.mainloop()

    def write_char_to_buffer(self, char):
        self.buffer_cache, submit = self.buffer.write_char(char)
        if submit > 0:
            self.text += self.buffer_cache[:submit]
            self.buffer_cache = ''
            return True
        return False

    def on_key_release(self, event):
        if len(event.keysym) == 1:
            replace = self.write_char_to_buffer(event.keysym)
        elif event.keysym == 'space':
            replace = self.write_char_to_buffer(' ')
        elif event.keysym == 'KP_Delete' or event.keysym == 'period':
            replace = self.write_char_to_buffer('.')
        elif event.keysym == 'BackSpace':
            if len(self.buffer_cache) > 0:
                self.buffer.pop_char()
            else:
                self.text = self.text[:-1]
                stop_token_index = -1
                for stop_token in Buffer.STOP_TOKENS:
                    try:
                        idx = self.text.rindex(stop_token)
                    except ValueError:
                        continue
                    stop_token_index = max(stop_token_index, idx)
                if stop_token_index != -1:
                    self.buffer_cache = self.buffer.set_without_processing(self.text[stop_token_index + 1:])
                    self.text = self.text[:stop_token_index + 1]
            replace = False
        else:
            print(event.keysym)
            replace = False
        if replace:
            self.text_box.replace('1.0', END, self.text + self.buffer_cache)