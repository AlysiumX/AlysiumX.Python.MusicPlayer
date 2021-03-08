import tkinter as root


class MainWindow:
    def __init__(self):
        self.window = root.Tk()
        self.window.title("Music Player")
        self.window.geometry("600x400")
        self.views = []

    def load_all_views(self):
        pass

    def add_view(self, view):
        self.views.append(view)

    def set_view(self, view):
        for loadedView in self.views:
            loadedView.hide()

        view.show()
        self.window.mainloop()
