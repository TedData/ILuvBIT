import tkinter as tk


def show_colours(colours, rows, font_size):
    root = tk.Tk()

    for i, (name, code) in enumerate(colours.items()):
        label = tk.Label(text=name, bg=code, font=('Arial', font_size),
                         width=20, height=5)
        label.grid(row=i // rows, column=i % rows)

        root.columnconfigure(i % rows, weight=1)

    root.mainloop()
