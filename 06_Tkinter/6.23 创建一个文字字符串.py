from tkinter import *
win = Tk()
canvas = Canvas(win)
canvas.create_text(40, 40, text="秋风起兮白云飞，草木黄落兮雁南归。", fill="red", anchor=W)
canvas.pack()
win.mainloop()
