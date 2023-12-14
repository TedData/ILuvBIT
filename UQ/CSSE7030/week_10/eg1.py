# Using a text widget - with a file menu and filedialog

import tkinter as tk 
from tkinter import filedialog

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 10")
        self._text = tk.Text(self._master)
        self._text.pack(expand=1, fill=tk.BOTH)
        

        # File menu
        menubar = tk.Menu(self._master)
        # tell master what it's menu is
        self._master.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        self._filename = None

    def new_file(self):
        self._text.delete("1.0", tk.END)
        self._filename = None
        self._master.title("New File")

    def save_file(self):
        if self._filename is None:
            filename = filedialog.asksaveasfilename()
            if filename:
                self._filename = filename
        if self._filename:
            self._master.title(self._filename)
            fd = open(self._filename, 'w')
            fd.write(self._text.get("1.0", tk.END))
            fd.close()
            

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self._filename = filename
            self._master.title(self._filename)
            fd = open(filename, 'r')
            self._text.insert(tk.INSERT, fd.read())
            fd.close()
                
root = tk.Tk()
app = App(root)
root.mainloop()
