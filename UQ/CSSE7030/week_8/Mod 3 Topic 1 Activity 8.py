import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Activity 8")
        self._master.geometry("600x400")

        self._frame = tk.Frame(self._master)
        # pack the frame
        self._frame.pack(expand=1)
        
        # put three labels in frame
        
        self._label1 = tk.Label(self._frame, text="Label 1")
        # pack it
        self._label1.pack(side=tk.LEFT)

        self._label2 = tk.Label(self._frame, text="Label 2")
        # pack it
        self._label2.pack(side=tk.LEFT)

        self._label3 = tk.Label(self._frame, text="Label 3")
        # pack it
        self._label3.pack(side=tk.LEFT) 
        

root = tk.Tk()
app = App(root)
root.mainloop()
