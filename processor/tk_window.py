from tkinter import *
import tkinter.filedialog as filedialog
from processor.buffer import Buffer


class TkWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('grammarly-0')

        menubar = Menu(self.root)

        filemenu = Menu(menubar)
        filemenu.add_command(label='New', command=self.clear_text_box)
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        self.text_box = Text(self.root)
        self.text_box.pack()
        self.button = Button(self.root, text='Correct', command=self.submit)
        self.button.pack()
        self.root.config(menu=menubar)
        self.root.mainloop()

    def submit(self):
        correct_text = ''
        text = self.text_box.get('1.0', END)
        buffer = Buffer()
        for c in text:
            buffer_cache, submit, add_space = buffer.write_char(c)
            if submit > 0:
                if add_space:
                    correct_text += ' '
                correct_text += buffer_cache

        self.text_box.replace('1.0', END, correct_text)

    def clear_text_box(self):
        self.text_box.replace('1.0', END, '')

    def open_file(self):
        try:
            with filedialog.askopenfile(mode='r') as f:
                self.text_box.replace('1.0', END, f.read())
        except TypeError:
            pass

    def save_file(self):
        try:
            with filedialog.asksaveasfile(mode='w') as f:
                f.write(self.text_box.get('1.0', END))
        except TypeError:
            pass
