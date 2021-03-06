import pygame as pg


class Player:
    def __init__(self):
        pg.init()

    # TODO : Figure out if I should be marking these static
    def play(self, song):
        pg.mixer.music.load(song)
        pg.mixer.music.play()

    def stop(self):
        pg.mixer.music.stop()
