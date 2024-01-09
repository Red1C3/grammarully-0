from tkinter import *
from processor.buffer import Buffer


class TkWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('grammarly-0')
        self.text_box = Text(self.root)
        self.text_box.pack()
        self.button = Button(self.root, text='Correct', command=self.submit)
        self.button.pack()
        self.root.mainloop()

    def submit(self):
        correct_text = ''
        text = self.text_box.get('1.0',END)
        buffer = Buffer()
        for c in text:
            buffer_cache, submit, add_space = buffer.write_char(c)
            if submit > 0:
                if add_space:
                    correct_text += ' '
                correct_text += buffer_cache

        self.text_box.replace('1.0', END, correct_text)
