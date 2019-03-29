from tkinter import *
win = Tk()
coord = 10, 50, 240, 210
canvas = Canvas(win)
canvas.create_arc(coord, start=0, extent=270, fill="blue")
canvas.pack()
win.mainloop()
