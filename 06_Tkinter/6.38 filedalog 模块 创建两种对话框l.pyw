from tkinter import *
import tkinter.filedialog

#创建主窗口
win = Tk()
win.title(string = "打开文件和保存文件")

#打开一个[打开旧文件]对话框
def createOpenFileDialog():
    myDialog1.show() 

#打开一个[另存新文件]对话框
def createSaveAsDialog():
    myDialog2.show() 

#按下按钮后,即打开对话框
Button(win, text="打开文件", command=createOpenFileDialog).pack(side=LEFT)
Button(win, text="保存文件",command=createSaveAsDialog).pack(side=LEFT)

#设置对话框打开的文件类型
myFileTypes = [('Python files', '*.py *.pyw'), ('All files', '*')] 

#创建一个[打开旧文件]对话框
myDialog1 = tkinter.filedialog.Open(win, filetypes=myFileTypes)
#创建一个[另存新文件]对话框
myDialog2 = tkinter.filedialog.SaveAs(win, filetypes=myFileTypes)

#开始程序循环
win.mainloop()
