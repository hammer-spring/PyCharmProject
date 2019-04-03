from tkinter import *
import tkinter.messagebox
#创建主窗口
win = Tk()

#执行菜单命令,显示一个对话框
def doSomething():
    tkinter.messagebox.askokcancel("菜单", "您正在选择菜单命令")

#创建一个主目录(toplevel)
mainmenu = Menu(win)
#新增菜单项
mainmenu.add_command(label="文件", command=doSomething)
mainmenu.add_command(label="编辑", command=doSomething)
mainmenu.add_command(label="视图", command=doSomething)
mainmenu.add_command(label="窗口", command=doSomething)
mainmenu.add_command(label="帮助", command=doSomething)

#设置主窗口的菜单
win.config(menu=mainmenu)

#开始程序循环
win.mainloop()
