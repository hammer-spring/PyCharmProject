from tkinter import *
win =Tk()
canvas = Canvas(win)
canvas.create_polygon(10, 10, 320, 80, 210, 230, outline="blue", splinesteps=1,fill="green")
canvas.pack()
win.mainloop()
