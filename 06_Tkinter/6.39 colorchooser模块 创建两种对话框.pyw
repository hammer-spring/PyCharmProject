from tkinter import *
import tkinter.colorchooser, tkinter.messagebox

#创建主窗口
win = Tk()
win.title(string = "颜色对话框")

#打开一个[颜色]对话框
def openColorDialog():
    #显示[颜色]对话框
    color = colorDialog.show()
    #显示所选择颜色的R,G,B值
    tkinter.messagebox.showinfo("提示", "您选择的颜色是：" + color[1] + "\n" + \
        "R = " + str(color[0][0]) + " G = " + str(color[0][1]) + " B = " + str(color[0][2]))
        
#按下按钮后,即打开对话框
Button(win, text="打开颜色对话框", \
    command=openColorDialog).pack(side=LEFT)

#创建一个[颜色]对话框
colorDialog = tkinter.colorchooser.Chooser(win)

#开始程序循环
win.mainloop()
