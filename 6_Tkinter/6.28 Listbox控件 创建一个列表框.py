from tkinter import *
win = Tk()

#创建窗体
frame = Frame(win)      

#创建列表框选项列表         
name = ["香蕉", "苹果", "橘子", "西瓜", "桃子", "菠萝", "柚子", "橙子"] 

#创建Listbox控件
listbox = Listbox(frame)
#清除Listbox控件的内容
listbox.delete(0, END)
#在Listbox控件内插入选项
for i in range(8):
    listbox.insert(END, name[i])

listbox.pack()
frame.pack()

#开始程序循环
win.mainloop()
