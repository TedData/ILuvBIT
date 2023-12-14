import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Activity 6")
        self._master.geometry("600x400")

        # create a button
        self._button = tk.Button(self._master, text="Button",bg="blue",
                                 command=self.press_me)
        # pack it
        self._button.pack(side=tk.RIGHT)
        
    def press_me(self):
        self._button.config(bg="red")


root = tk.Tk()
app = App(root)
root.mainloop()
