from tkinter import *

#创建主窗口
win = Tk()

txt = "暮云收尽溢清寒，银汉无声转玉盘。此生此夜不长好，明月明年何处看。"
msg = Message(win, text=txt)
msg.pack()

#开始程序循环
win.mainloop()
