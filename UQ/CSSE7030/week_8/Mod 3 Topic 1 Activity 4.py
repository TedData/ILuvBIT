import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Activity 4")
        self._master.geometry("600x400")
        self._label1 = tk.Label(self._master, text="Label 1", bg="orange")
        self._label1.pack() #same as pack(side=tk.TOP)
        self._label2 = tk.Label(self._master, text="Label 2", bg="blue")
        self._label2.pack(side=tk.BOTTOM)


root = tk.Tk()
app = App(root)
root.mainloop()
