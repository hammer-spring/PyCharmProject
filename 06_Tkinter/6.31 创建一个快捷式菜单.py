from tkinter import *
import tkinter.messagebox
#创建主窗口
win = Tk()

#执行菜单命令,显示一个对话框
def doSomething():
    tkinter.messagebox.askokcancel ("菜单", "您正在选择快捷式菜单命令")

#创建一个快捷式菜单(pop-up)
popupmenu = Menu(win, tearoff=0)

#新增快捷式菜单的项目
popupmenu.add_command(label="复制", command=doSomething)
popupmenu.add_command(label="粘贴", command=doSomething)
popupmenu.add_command(label="剪切", command=doSomething)
popupmenu.add_command(label="删除", command=doSomething)

#在单击鼠标右键的窗口(x,y)坐标处,显示此快捷式菜单
def showPopUpMenu(event):
    popupmenu.post(event.x_root, event.y_root)

#设置单击鼠标右键后,显示此快捷式菜单
win.bind("<Button-3>", showPopUpMenu)

#开始程序循环
win.mainloop()
