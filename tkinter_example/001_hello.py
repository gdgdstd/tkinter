import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello Tkinter Example")


if __name__ == "__main__":
    app = App()
    app.mainloop()