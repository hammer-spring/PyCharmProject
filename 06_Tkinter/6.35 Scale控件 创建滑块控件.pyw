from tkinter import *
from string import *

#创建主窗口
win = Tk()

#将标尺上的0~100范围的数字,转换成0~255范围的16进位数字,
#再转换成2个字符的字符串,如果数字只有一位,就在前面加一个零
def getRGBStr(value):
    #将标尺上的0~100范围的数字,转换成0~255范围的16进位数字,
#再转换成字符串
    ret = str(hex(int(value/100*255)))
    #将16进位数字前面的0x去掉
    ret = ret[2:4]
    #转换成2个字符的字符串,如果数字只有一位,就在前面加一个零
    ret = zfill(ret, 2)   
    return ret

#将RGB颜色的字符串,转换成#rrggbb类型的字符串
def showRGBColor():
    #读取#rrggbb字符串的rr部分
    strR = getRGBStr(var1.get())
    #读取#rrggbb字符串的gg部分
    strG = getRGBStr(var2.get())
    #读取#rrggbb字符串的bb部分
    strB = getRGBStr(var3.get())
    #转换成#rrggbb类型的字符串
    color = "#" + strR + strG + strB
    #将颜色字符串,设置给Label控件的背景颜色
    colorBar.config(background = color)

#分别读取三个标尺的值,是一个双精度浮点数
var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()

#创建标尺
scale1 = Scale(win, variable=var1)
scale2 = Scale(win, variable=var2)
scale3 = Scale(win, variable=var3)

#将选择钮靠左对齐
scale1.pack(side=LEFT)
scale2.pack(side=LEFT)
scale3.pack(side=LEFT)

#创建一个标签,用来显示颜色字符串
colorBar = Label(win, text=" "*40, background="#000000")
colorBar.pack(side=TOP)

#创建一个按钮,按下后即将标尺上的RGB颜色显示在Label控件上
button = Button(win, text="查看颜色", command=showRGBColor)
button.pack(side=BOTTOM)

#开始程序循环
win.mainloop()
