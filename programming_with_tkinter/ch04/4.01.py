import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.option_readfile("./optionDB")

        self.title("顶层窗口演示")

        ttk.Label(self, text="这是默认的主窗口").pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
