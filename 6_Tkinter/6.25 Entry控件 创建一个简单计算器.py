from tkinter import *

win = Tk()
# 创建窗体
frame = Frame(win)


# 创建一个计算式
def calc():
    # 将用户输入的表达式,计算结果后转换成字符串
    result = "= " + str(eval(expression.get()))
    # 将计算的结果显示在Label控件上
    label.config(text=result)


# 创建一个Label控件
label = Label(frame)
# 创建一个Entry控件
entry = Entry(frame)

# 读取用户输入的表达式
expression = StringVar()
# 将用户输入的表达式显示在Entry控件上
entry["textvariable"] = expression

# 创建一个Button控件.当用户输入完毕后,按此钮即计算表达式的结果
button1 = Button(frame, text="等于", command=calc)

# 设置Entry控件为焦点所在
entry.focus()
frame.pack()
# Entry控件位在窗体的上方
entry.pack()
# Label控件位在窗体的左方
label.pack(side=LEFT)
# Button控件位在窗体的右方
button1.pack(side=RIGHT)

# 开始程序循环
frame.mainloop()
