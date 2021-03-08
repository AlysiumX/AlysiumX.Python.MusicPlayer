from tkinter import Button, Listbox, Frame
from views.open_file_dialog import OpenFileDialog
from Logic.player import Player


class PlayerView:
    directories = []

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.frame = Frame(parent_window.window)

        self.button_play = Button(self.frame, text=f"Play", command=self.__button_play_clicked)
        self.button_stop = Button(self.frame, text=f"Stop", command=self.__button_stop_clicked)
        self.button_open = Button(self.frame, text=f"Open", command=self.__button_open_clicked)
        self.song_list = Listbox(self.frame)
        self.player = Player()

        self.song_list.grid(column=0, row=0)

        self.button_open.config(width=8)
        self.button_open.grid(column=0, row=1)

        self.button_stop.config(width=8)
        self.button_stop.grid(column=1, row=1)

        self.button_play.config(width=8)
        self.button_play.grid(column=2, row=1)

    def show(self):
        self.frame.grid(column=0, row=0)

    def hide(self):
        self.frame.grid_forget()

    def __button_open_clicked(self):
        open_file_dialog = OpenFileDialog()
        self.directories = open_file_dialog.show()
        for index, directory in enumerate(self.directories):
            self.song_list.insert(index, directory)

    def __button_play_clicked(self):
        if self.song_list.curselection():
            selected_song = self.song_list.get(self.song_list.curselection())
            self.player.play(selected_song)

    def __button_stop_clicked(self):
        self.player.stop()

