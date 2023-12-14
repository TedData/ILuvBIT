# Use anchor

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 7")
        self._master.geometry("300x200")
        self._label1 = tk.Label(self._master, text="A label", bg="green")

        self._label1.pack(side=tk.LEFT,expand=1) 
        self._label2 = tk.Label(self._master, text="A label", bg="green")

        self._label2.pack(side=tk.LEFT,expand=1) 
        

        self._button1 = tk.Button(self._master, text="Press Me",fg="green",
                                 command=self.press_me)

        self._button1.pack(fill=tk.BOTH)
        self._button2 = tk.Button(self._master, text="Press Me",fg="green",
                                 command=self.press_me)

        self._button2.pack()
        





        self._state = False







    def redraw(self):
        if self._state:
            self._button1.config(text="Press Me Again", fg="red")
            self._label1.config(bg="red")
        else:
            self._button1.config(text="Press Me", fg="green")
            self._label1.config(bg="green")
            
        
    def press_me(self):
        self._state = not self._state
        self.redraw()


root = tk.Tk()
app = App(root)
root.mainloop()
