# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:26:42 2020

@author: Unknown
"""

import tkinter as tk


class AppData:
    def __init__(self):
        """
        Class that shares data between all the other classes.

        Returns
        -------
        None.

        """
        self.titles = []
        self.sites = []


class InfoPane(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Shows the information of the titles and sites.

        Parameters
        ----------
        parent : TYPE
            DESCRIPTION.
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.titles = []
        self.sites = []

    def buildList(self, titles, sites):
        """
        This might actually need to be within the AppData class instead.

        Parameters
        ----------
        titles : TYPE
            DESCRIPTION.
        sites : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.parent.data.titles.append(tk.Label(self, text='Test'))
        self.parent.data.sites.append(tk.Button(self, text='URL', command=lambda: print('URL pressed!')))

        # Another example of what's possible, not necessarily the right way to do it though
        self.popList()

    def popList(self):
        """
        This could be called after the observer sees that the sites and titles lists have been populated

        Returns
        -------
        None.

        """
        self.parent.data.titles[0].grid(row=0, column=0)
        self.parent.data.sites[0].grid(row=0, column=1)


class Navbar(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        """
        Standard navigation bar.

        Parameters
        ----------
        parent : TYPE
            DESCRIPTION.
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(*args, **kwargs)
        self.parent = parent

        file = tk.Menu(self, tearoff=0)
        file.add_command(label="New", command=lambda: print('new'))
        file.add_command(label="Open", command=lambda: print('open'))
        file.add_command(label="Save", command=lambda: print('save'))
        file.add_command(label='Read CSV', command=lambda: print('reading CSV...'))
        # Don't necessarily like this way of calling buildList but it is left here as an example of how the list could
        # be built
        file.add_command(label='Build List', command=lambda: self.parent.infopane.buildList(1, 1))
        file.add_separator()
        file.add_command(label="Exit", command=lambda: print('Not actually quitting'))

        self.add_cascade(label="File", menu=file)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Main application.

        Parameters
        ----------
        parent : TYPE
            DESCRIPTION.
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.data = AppData()

        self.navbar = Navbar(self)
        self.infopane = InfoPane(self)

        self.parent.config(menu=self.navbar)

        self.infopane.pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.geometry('900x400')
    root.mainloop()
