from tkinter import *
import tkinter.filedialog
from PIL import Image

#创建主窗口
win = Tk()
win.title(string = "图像文件的属性")

#打开一个[打开旧文件]对话框
def createOpenFileDialog():
    #返回打开的文件名
    filename = myDialog.show() 
    #打开该文件
    imgFile = Image.open(filename)
    #填入该文件的属性
    label1.config(text = "format = " + imgFile.format)
    label2.config(text = "mode = " + imgFile.mode)
    label3.config(text = "size = " + str(imgFile.size)) 
    label4.config(text = "info = " + str(imgFile.info))

#创建Label控件, 用来填入图像文件的属性
label1 = Label(win, text = "format = ")
label2 = Label(win, text = "mode = ")
label3 = Label(win, text = "size = ")
label4 = Label(win, text = "info = ")
#靠左边对齐
label1.pack(anchor=W)
label2.pack(anchor=W)
label3.pack(anchor=W)
label4.pack(anchor=W)

#按下按钮后,即打开对话框
Button(win, text="打开图像文件",command=createOpenFileDialog).pack(anchor=CENTER)

#设置对话框打开的文件类型
myFileTypes = [('Graphics Interchange Format', '*.gif'), ('Windows bitmap', '*.bmp'),
    ('JPEG format', '*.jpg'), ('Tag Image File Format', '*.tif'), 
    ('All image files', '*.gif *.jpg *.bmp *.tif')] 

#创建一个[打开旧文件]对话框
myDialog = tkinter.filedialog.Open(win, filetypes=my FileTypes)

#开始程序循环
win.mainloop()
