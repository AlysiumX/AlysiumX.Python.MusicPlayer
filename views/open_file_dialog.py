from tkinter import filedialog as fd


class OpenFileDialog:
    def __init__(self):
        self.filetypes = (
            ('Music files', '*.mp3'),
            ('All files', '*.*')
        )
        self.filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=self.filetypes)

    def show(self):
        return self.filenames

