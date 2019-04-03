from tkinter import *
win = Tk()

#设置图片文件的路径
path = "D:\\PyCharm\\PyCharmProject\\06_Tkinter\\"
img = []
#将9张图片放入一个列表中
for i in range(9):
    img.append(PhotoImage(file=path + "a" + str(i) + ".gif"))

#创建9个窗体
frame = []
for i in range(3):
    for j in range(3):
        frame.append(Frame(win, relief=RAISED, borderwidth=1, width=158,height=112))
        #创建9个Label控件
        Label(frame[j+i*3], image=img[j+i*3]).pack()
        #将窗体编排成3×3的表格
        frame[j+i*3].grid(row=j, column=i)

#开始程序循环
win.mainloop()
