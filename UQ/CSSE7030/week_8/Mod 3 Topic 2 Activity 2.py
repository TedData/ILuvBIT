import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Activity 2")
        self._master.geometry("600x400")
        self._label = tk.Label(self._master, text="Label 1", bg="blue")
        # pack it
        self._label.pack()
        
        self._state = False
        self.animation()

    def animation(self):
        self._state=not self._state
        if self._state:
            self._label.config(bg="blue")
        else:
            self._label.config(bg="red")
            
        # wait 2000 milliseconds (two seconds) and then call self.animation()
        self._master.after(2000,self.animation)


root = tk.Tk()
app = App(root)
root.mainloop()
