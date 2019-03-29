from tkinter import *
import tkinter.filedialog, struct

#创建应用程序的类
class App:
    def __init__(self, master):
        #创建一个Label配件
        self.label = Label(master)
        self.label.pack(anchor=W) 
        #创建一个Button配件
        self.button = Button(master, text="Start", command=self.getBinaryData)
        self.button.pack(anchor=CENTER)

    def setBinaryData(self):  
        #将数值数据100, 200, 300, 400, 转换成integer类型的二进制数据 
        self.bytes = struct.pack("i"*4, 100, 200, 300, 400)

    def getBinaryData(self):
        self.setBinaryData()
        #将integer类型的二进制数据, 转换成原来的数值数据(100, 200, 300, 400)  
        values = struct.unpack("i"*4, self.bytes)
        self.label.config(text = str(values))
        
#创建应用程序窗口
win = Tk()
win.title(string = "平面数据库")

#创建应用程序类的实例变量
app = App(win)

#开始程序循环
win.mainloop()
