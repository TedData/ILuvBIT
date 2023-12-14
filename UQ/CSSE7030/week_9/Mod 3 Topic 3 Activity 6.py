#when click on canvas the first time a square is drawn,
#the second time a circle is drawn,
#the third time a triangle is drawn.

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        master.title("Activity 6")
        master.geometry("400x600")
        self._canvas = tk.Canvas(master, bg='white')
        self._canvas.pack(expand=1,fill=tk.BOTH)
        self._canvas.bind("<Button-1>", self.press1)
        
        self._shape = 0

    def press1(self, e):
        d = 80

        if self._shape == 0:
            #draw a square
            self._canvas.create_rectangle([(e.x, e.y), (e.x+d, e.y+d)])
        elif self._shape == 1:
            #draw a circle
            self._canvas.create_oval([(e.x, e.y), (e.x+d, e.y+d)])
        elif self._shape == 2:
            #draw a triangle
            #create_polygon([x, y, x2, y2, x3, y3], outline=?, fill=?)
            #by default, does not have outline and fill is black. so need to change that.
            self._canvas.create_polygon([e.x, e.y, e.x-d/2, e.y+d, e.x+d/2, e.y+d], outline = "black", fill="")
        
        self._shape += 1
        if self._shape > 2:
            self._shape = 0


root = tk.Tk()
app = App(root)
root.mainloop()
