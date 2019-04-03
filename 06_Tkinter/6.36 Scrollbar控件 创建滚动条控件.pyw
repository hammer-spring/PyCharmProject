from tkinter import *

#创建主窗口
win = Tk()

#创建一个水平滚动条
scrollbar1 = Scrollbar(win, orient=HORIZONTAL)
#水平滚动条位在窗口底端,当窗口改变大小时会在X方向填满窗口
scrollbar1.pack(side=BOTTOM, fill=X)

#创建一个垂直滚动条
scrollbar2 = Scrollbar(win)
#垂直滚动条位在窗口右端,当窗口改变大小时会在Y方向填满窗口
scrollbar2.pack(side=RIGHT, fill=Y)

#创建一个列表框,x方向的滚动条指令是scrollbar1对象的set()方法,
#y方向的滚动条指令是scrollbar2对象的set()方法
mylist = Listbox(win, xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set)
#在列表框内插入60个选项
for i in range(60):
    mylist.insert(END, "火树银花合，星桥铁锁开。暗尘随马去，明月逐人来。" + str(i))
#列表框位于窗口左端,当窗口改变大小时会在X与Y方向填满窗口
mylist.pack(side=LEFT, fill=BOTH)

#移动水平滚动条时,改变列表框的x方向可见范围
scrollbar1.config(command=mylist.xview)
#移动垂直滚动条时,改变列表框的y方向可见范围
scrollbar2.config(command=mylist.yview)

#开始程序循环
win.mainloop()
