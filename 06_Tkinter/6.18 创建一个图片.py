from tkinter import *
win = Tk()
img = PhotoImage(file="10.1.gif")
canvas = Canvas(win)
canvas.create_image(140, 140, image=img)
canvas.pack()
win.mainloop()
