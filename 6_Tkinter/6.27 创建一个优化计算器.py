from tkinter import *
win = Tk()	
#创建窗体
frame = Frame(win)

#创建一个计算式
def calc():
    #将用户输入的表达式,计算结果后转换成字符串
    result = "= " + str(eval(expression.get()))
    #将计算的结果显示在Label widget上
    label.config(text = result)

#清除文本框与文字标签的内容
def clear():
    expression.set("")
    label.config(text = "")

#创建一个Label控件
label = Label(frame)
#读取用户输入的表达式
expression = StringVar()
#创建一个Entry控件, Entry控件位在窗体的上方
entry = Entry(frame, textvariable=expression)
entry.pack()

#创建一个Button控件.当用户输入完毕后,按此钮即计算表达式的结果
button1 = Button(frame, text="等于", command=calc)
button2 = Button(frame, text="清除", command=clear)

#设置Entry控件为焦点所在
entry.focus()
frame.pack()
#Label控件位在窗体的左方
label.pack(side=LEFT)
#Button控件位在窗体的右方
button1.pack(side=RIGHT)
button2.pack(side=RIGHT)

#开始程序循环
frame.mainloop()
