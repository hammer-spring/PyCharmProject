from tkinter import *
win = Tk()
win.title(string = "古诗鉴赏")
Label(win,text="花间一壶酒，独酌无相亲。举杯邀明月，对影成三人。").pack()
Button(win,text="关闭",command=win.quit).pack(side="bottom")
win.mainloop()