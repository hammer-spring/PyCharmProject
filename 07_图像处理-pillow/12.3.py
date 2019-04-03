from tkinter import *
from PIL import Image, ImageTk

#创建主窗口
win = Tk()
win.title(string = "复制与粘贴图像")

#打开图像文件
path = "D:\\python\\ch12\\"
imgFile = Image.open(path + "12.2.jpg")

#创建第一个图像实例变量
img1 = ImageTk.PhotoImage(imgFile)

#读取图像文件的宽与高
width, height = imgFile.size
#设置剪下的区块范围
box1 = (0, 0, width, int(height/2))

#将图像的上半部剪下
part = imgFile.crop(box1)
#将
part= part.transpose(Image.ROTATE_180)
#将图像得上半部粘贴到上半部
imgFile.paste(part, box1)

#创建第二个图像实例变量
img2 = ImageTk.PhotoImage(imgFile)

#创建Label控件,来显示图像
label1 = Label(win, width=400, height=400, image=img1, borderwidth=1)
label2 = Label(win, width=400, height=400, image=img2, borderwidth=1)
label1.pack(side=LEFT)
label2.pack(side=LEFT)

#开始程序循环
win.mainloop()
