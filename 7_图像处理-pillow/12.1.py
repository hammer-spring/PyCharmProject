from tkinter import *
from PIL import Image, ImageTk

#创建主窗口
win = Tk()
win.title(string = "加载图像文件")

path = "D:\\python\\ch12\\"
imgFile1 = Image.open(path + "12.1.gif")
imgFile2 = Image.open(path + "12.1.jpg")
imgFile3 = Image.open(path + "12.1.bmp")
imgFile4 = Image.open(path + "12.1.tif")

img1 = ImageTk.PhotoImage(imgFile1)
img2 = ImageTk.PhotoImage(imgFile2)
img3 = ImageTk.PhotoImage(imgFile3)
img4 = ImageTk.PhotoImage(imgFile4)

canvas = Canvas(win, width=400, height=360)
canvas.create_image(40, 40, image=img1, anchor=NW)
canvas.create_image(220, 40, image=img2, anchor=NW)
canvas.create_image(40, 190, image=img3, anchor=NW)
canvas.create_image(220, 190, image=img4, anchor=NW)
canvas.pack(fill=BOTH)

#开始程序循环
win.mainloop()
保存并运行程序，结果如图10-8所示：
