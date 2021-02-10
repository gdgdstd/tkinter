from tkinter import *


def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand="yes", fill="both", padx=5, pady=5)
    return w


def button(root, side, text, command=None):
    w = Button(
        root,
        text=text,
        command=command,
        bd=5,
        bg="#8d998d",
        fg="white",
        font="vertical 24 bold",
    )
    w.pack(side=side, expand="yes", fill="both")
    return w


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("简单的计算器")

        self.display = StringVar()
        Entry(
            self,
            relief="sunken",
            bd=5,
            bg="#8d998d",
            fg="white",
            font="vertical 24 bold",
            textvar=self.display,
        ).pack(expand="yes", fill="both", padx=5)

        for key in "123 456 789 -0.".split():
            kf = key_frame = frame(self, "top")
            for char in key:
                button(
                    kf,
                    "left",
                    char,
                    lambda w=self.display, s=f"{char}": w.set(w.get() + s),
                )
        of = operator_frame = frame(self, "top")
        for char in "+-*/=":
            if char == "=":
                btn = button(of, "left", char)
                btn.bind("<ButtonRelease-1>", lambda e, s=self: s.calc(), "+")
            else:
                btn = button(
                    of,
                    "left",
                    char,
                    lambda w=self.display, c=char: w.set(w.get() + " " + c + " "),
                )

        cf = clear_frame = frame(self, "top")
        button(cf, "left", "CLR", lambda w=self.display: w.set(""))

    def calc(self):
        try:
            self.display.set(eval(self.display.get()))
        except ValueError:
            self.display.set("#ERR")
            
        except SyntaxError:
            self.display.set("#ERR")
            


if __name__ == "__main__":
    app = App()
    app.mainloop()
