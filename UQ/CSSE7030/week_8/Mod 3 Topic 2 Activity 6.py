# Using a canvas and events

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 11")
        self._master.geometry("600x400")
        self._canvas = tk.Canvas(self._master, bg='orange')
        self._canvas.pack()
        self._canvas.bind("<Button-1>", self.press1)
        self._canvas.bind("<B1-Motion>", self.motion1)
        self._canvas.bind("<ButtonRelease-1>", self.release1)
        self._canvas.bind_all("<Key>", self.key_press)

        self._x_position = -1
        self._y_position = -1

    def press1(self, e):
        print("press", e.x, e.y)

    def motion1(self, e):
        if (self._x_position == -1):
            #first time method called
            self._x_position = e.x
            self._y_position = e.y
        else:
            print("distance travelled: ", ((e.x - self._x_position)**2 + (e.y - self._y_position)**2)**(1/2))
            #update the positions
            self._x_position = e.x
            self._y_position = e.y

    def release1(self, e):
        print("release", e.x, e.y)

    def key_press(self, e):
        print(e.char, e.keysym, e.keycode)


root = tk.Tk()
app = App(root)
root.mainloop()
