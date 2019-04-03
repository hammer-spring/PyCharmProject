from tkinter import *
from PIL import Image, ImageTk

#创建主窗口
win = Tk()
win.title(string = "图像的几何转换")

#打开图像文件
path = "D:\\python\\ch12\\"
imgFile1 = Image.open(path + "12.3.gif")

#创建第一个图像实例变量
img1 = ImageTk.PhotoImage(imgFile1)

#创建Label控件,来显示原始图像
label1 = Label(win, width=162, height=160, image=img1)
label1.pack(side=LEFT)

#旋转图像成45°角
imgFile2 = imgFile1.rotate(45)
img2 = ImageTk.PhotoImage(imgFile2)
#创建Label控件,来显示图像
label2 = Label(win, width=162, height=160, image=img2)
label2.pack(side=LEFT)

#旋转图像成90°角
imgFile3 = imgFile1.transpose(Image.ROTATE_90)
img3 = ImageTk.PhotoImage(imgFile3)
#创建Label控件,来显示图像
label3 = Label(win, width=162, height=160, image=img3)
label3.pack(side=LEFT)

#改变图像大小为1 / 4倍
width, height = imgFile1.size
imgFile4 = imgFile1.resize((int(width/2), int(height/2)))
img4 = ImageTk.PhotoImage(imgFile4)
#创建Label控件,来显示原始图像
label4 = Label(win, width=162, height=160, image=img4)
label4.pack(side=LEFT)

#开始程序循环
win.mainloop()
