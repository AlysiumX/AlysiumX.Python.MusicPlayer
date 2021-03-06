import tkinter as root
from tkinter import Button, Listbox
from views.open_file_dialog import OpenFileDialog
from Logic.player import Player


class PlayerView:
    directories = []

    def __init__(self):
        self.window = root.Tk()
        self.button_play = Button(self.window, text=f"Play", command=self.__button_play_clicked)
        self.button_stop = Button(self.window, text=f"Stop", command=self.__button_stop_clicked)
        self.button_open = Button(self.window, text=f"Open", command=self.__button_open_clicked)
        self.song_list = Listbox(self.window)
        self.player = Player()

    def __button_open_clicked(self):
        open_file_dialog = OpenFileDialog()
        self.directories = open_file_dialog.show()
        for index, directory in enumerate(self.directories):
            self.song_list.insert(index, directory)

    def __button_play_clicked(self):
        selected_song = self.song_list.get(self.song_list.curselection())
        self.player.play(selected_song)

    def __button_stop_clicked(self):
        self.player.stop()

    def show(self):
        self.window.title("Music Player")
        self.window.geometry("600x400")

        self.song_list.grid(column=0, row=0)

        self.button_open.config(width=8)
        self.button_open.grid(column=0, row=1)

        self.button_stop.config(width=8)
        self.button_stop.grid(column=1, row=1)

        self.button_play.config(width=8)
        self.button_play.grid(column=2, row=1)

        self.window.mainloop()
