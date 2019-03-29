from tkinter import *
import tkinter.messagebox

#处理WM_DELETE_WINDOW事件
def handleProtocol():
    #打开一个[确定/取消]对话框
    if tkinter.messagebox.askokcancel("提示", "您确定要关闭窗口吗？"):
       #确定要结束应用程序
       win.destroy()

#创建主窗口
win = Tk()

#创建协议
win.protocol("WM_DELETE_WINDOW", handleProtocol)

#开始窗口的事件循环
win.mainloop()
