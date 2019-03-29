from tkinter import *
win = Tk()
canvas = Canvas(win)
canvas.create_oval(10, 10, 240, 240, fill="green", outline="blue")
canvas.pack()
win.mainloop()
