import tkinter as tk 

class App(object):
    def __init__(self, master, title):
        self._master=master
        self._master.title(title)

root1=tk.Tk()
app1 = App(root1, "Window 1")

root2=tk.Tk()
app2 = App(root2, "Window 2")

root1.mainloop()
root2.mainloop()
