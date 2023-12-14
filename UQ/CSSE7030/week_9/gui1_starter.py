"""
Simple GUI programming exercise to demonstrate component layout
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


import tkinter as tk


class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = tk.Label(master, text="Choose a button")
        self._lbl.pack(side=tk.TOP)

        btn = tk.Button(master, text="Click Me!", command=self.say_hello)
        btn.pack(side=tk.TOP)

    def say_hello(self) :
        print('Hello! Thanks for clicking!')


if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()
