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
#创建单选按钮
radio1 = Radiobutton(win, text=sports[0], variable=var,value=0,command=showSelection)
radio2 = Radiobutton(win, text=sports[1], variable=var, value=1, command=showSelection)
radio3 = Radiobutton(win, text=sports[2], variable=var, value=2, command=showSelection)
radio4 = Radiobutton(win, text=sports[3], variable=var, value=3,command=showSelection)
radio5 = Radiobutton(win, text=sports[4], variable=var, value=4,command=showSelection)

#将单选按钮的外型,设置成命令型按钮
radio1.config(indicatoron=0) 
radio2.config(indicatoron=0) 
radio3.config(indicatoron=0) 
radio4.config(indicatoron=0) 
radio5.config(indicatoron=0) 

#将单选按钮靠左边对齐
radio1.pack(anchor=W)
radio2.pack(anchor=W) 
radio3.pack(anchor=W) 
radio4.pack(anchor=W) 
radio5.pack(anchor=W) 

#创建文字标签,用来显示用户的选择
label = Label(win)
label.pack()

#开始程序循环
win.mainloop()
