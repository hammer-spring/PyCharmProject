from tkinter import *
win = Tk()
canvas = Canvas(win)
canvas.create_line(10, 10, 40, 120, 230, 270, width=3, fill="green")
canvas.pack()
win.mainloop()
