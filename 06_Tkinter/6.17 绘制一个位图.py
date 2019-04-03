from tkinter import *
win =Tk()
canvas = Canvas(win)
canvas.create_bitmap(40, 40, bitmap="warning")
canvas.pack()
win.mainloop()

