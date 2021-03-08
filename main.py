# import tkinter as tk
#
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

from views.playerview import PlayerView
from mainwindow import MainWindow

main_window = MainWindow()

player_view = PlayerView(main_window)
main_window.add_view(player_view)
main_window.set_view(player_view)

# player_view = PlayerView()
# player_view.show()
