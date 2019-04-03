from tkinter import *
#创建主窗口
win = Tk()

#运动项目列表
sports = ["棒球", "篮球", "足球", "网球", "排球"]

#将用户的选择,显示在Label控件上
def showSelection():
    choice = "您的选择是：" + sports[var.get()]
    label.config(text = choice)

#读取用户的选择值,是一个整数
var = IntVar()
#创建单选按钮,靠西边对齐
Radiobutton(win, text=sports[0], variable=var, value=0,command=showSelection).pack(anchor=W)
Radiobutton(win, text=sports[1], variable=var, value=1,command=showSelection).pack(anchor=W)
Radiobutton(win, text=sports[2], variable=var, value=2,command=showSelection).pack(anchor=W)
Radiobutton(win, text=sports[3], variable=var, value=3,command=showSelection).pack(anchor=W)
Radiobutton(win, text=sports[4], variable=var, value=4,command=showSelection).pack(anchor=W)

#创建文字标签,用来显示用户的选择
label = Label(win)
label.pack()

#开始程序循环
win.mainloop()
