from tkinter import *

# 主窗口
win = Tk()

# 创建窗体
frame = Frame(win, relief=RAISED, borderwidth=2, width=400, height=300)
frame.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, expand=1)

# 第1个按钮的位置在距离窗体左上角的(40, 40)坐标处
button1 = Button(frame, text="Button 1")
button1.place(x=40, y=40, anchor=W, width=80, height=40)

# 第2个按钮的位置在距离窗体左上角的(140, 80)坐标处
button2 = Button(frame, text="Button 2")
button2.place(x=140, y=80, anchor=W, width=80, height=40)

# 开始窗口的事件循环
win.mainloop()
