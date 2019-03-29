from tkinter import *
import tkinter.messagebox

#创建主窗口
win = Tk()

#执行[文件/新建]菜单命令,显示一个对话框
def doFileNewCommand(*arg):
    tkinter.messagebox.askokcancel("菜单", "您正在选择【新建】菜单命令")

#执行[文件/打开]菜单命令,显示一个对话框
def doFileOpenCommand(*arg):
    tkinter.messagebox.askokcancel ("菜单", "您正在选择【打开】菜单命令")

#执行[文件/保存]菜单命令,显示一个对话框
def doFileSaveCommand(*arg):
   tkinter.messagebox.askokcancel ("菜单", "您正在选择【保存】菜单命令")

#执行[帮助/文档]菜单命令,显示一个对话框
def doHelpContentsCommand(*arg):
    tkinter.messagebox.askokcancel ("菜单", "您正在选择【保存】菜单命令")

#执行[帮助/文关于]菜单命令,显示一个对话框
def doHelpAboutCommand(*arg):
    tkinter.messagebox.askokcancel ("菜单", "您正在选择【关于】菜单命令")

#创建一个下拉式菜单(pull-down)
mainmenu = Menu(win)

#新增"文件"菜单的子菜单
filemenu = Menu(mainmenu, tearoff=0)
#新增"文件"菜单的菜单项
filemenu.add_command(label="新建", command=doFileNewCommand, accelerator="Ctrl-N")
filemenu.add_command(label="打开", command=doFileOpenCommand,accelerator="Ctrl-O")
filemenu.add_command(label="保存", command=doFileSaveCommand,accelerator="Ctrl-S")
filemenu.add_separator()
filemenu.add_command(label="退出", command=win.quit)
#新增"文件"菜单
mainmenu.add_cascade(label="文件", menu=filemenu)

#新增"帮助"菜单的子菜单
helpmenu = Menu(mainmenu, tearoff=0)
#新增"帮助"菜单的菜单项
helpmenu.add_command(label="文档", command=doHelpContentsCommand,accelerator="F1")
helpmenu.add_command(label="关于", command=doHelpAboutCommand,accelerator="Ctrl-A")
#新增"帮助"菜单
mainmenu.add_cascade(label="帮助", menu=helpmenu)

#设置主窗口的菜单
win.config(menu=mainmenu)

win.bind("<Control-n>", doFileNewCommand)
win.bind("<Control-N>", doFileNewCommand)
win.bind("<Control-o>", doFileOpenCommand)
win.bind("<Control-O>", doFileOpenCommand)
win.bind("<Control-s>", doFileSaveCommand)
win.bind("<Control-S>", doFileSaveCommand)
win.bind("<F1>", doHelpContentsCommand)
win.bind("<Control-a>", doHelpAboutCommand)
win.bind("<Control-A>", doHelpAboutCommand)

#开始程序循环
win.mainloop()
