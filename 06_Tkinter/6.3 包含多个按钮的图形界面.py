from tkinter import *
win = Tk()
Button(win, padx=20, text="关闭", command=win.quit).pack()
Button(win, padx="2c", text="关闭", command=win.quit).pack()
Button(win, padx="8m", text="关闭", command=win.quit).pack()
Button(win, padx="2i", text="关闭", command=win.quit).pack()
Button(win, padx="20p", text="关闭", command=win.quit).pack()
win.mainloop()
