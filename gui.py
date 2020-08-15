# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:26:42 2020

@author: Unknown
"""

import tkinter as tk


def donothing():
    pass


class Navbar(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        file = tk.Menu(self, tearoff=0)
        file.add_command(label="New", command=donothing)
        file.add_command(label="Open", command=donothing)
        file.add_command(label="Save", command=donothing)
        file.add_command(label='Read CSV', command=lambda: print('reading CSV...'))
        file.add_separator()
        file.add_command(label="Exit", command=lambda: print('Not actually quitting'))

        self.add_cascade(label="File", menu=file)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.navbar = Navbar(self)

        self.parent.config(menu=self.navbar)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
