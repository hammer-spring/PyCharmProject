from tkinter import *
win = Tk()
canvas = Canvas(win)
canvas.create_rectangle(10, 10, 220, 220, fill="red", outline="")
canvas.pack()
win.mainloop()
