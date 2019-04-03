from tkinter import *


# 处理鼠标光标进入窗体时的事件
def handleEnterEvent(event):
    label1["text"] = "You enter the frame"
    label2["text"] = ""
    label3["text"] = ""


# 处理鼠标光标离开窗体时的事件
def handleLeaveEvent(event):
    label1["text"] = "You leave the frame"
    label2["text"] = ""
    label3["text"] = ""


# 处理在窗体内单击鼠标左键的事件
def handleLeftButtonPressEvent(event):
    label1["text"] = "You press the left button"
    label2["text"] = "x = " + str(event.x)
    label3["text"] = "y = " + str(event.y)


# 处理在窗体内单击鼠标中间键的事件
def handleMiddleButtonPressEvent(event):
    label1["text"] = "You press the middle button"
    label2["text"] = "x = " + str(event.x)
    label3["text"] = "y = " + str(event.y)


# 处理在窗体内单击鼠标右键的事件
def handleRightButtonPressEvent(event):
    label1["text"] = "You press the right button"
    label2["text"] = "x = " + str(event.x)
    label3["text"] = "y = " + str(event.y)


# 处理在窗体内单击鼠标左键,然后移动鼠标光标的事件
def handleLeftButtonMoveEvent(event):
    label1["text"] = "You are moving mouse with the left button pressed"
    label2["text"] = "x = " + str(event.x)
    label3["text"] = "y = " + str(event.y)


# 处理在窗体内放开鼠标左键的事件
def handleLeftButtonReleaseEvent(event):
    label1["text"] = "You release the left button"
    label2["text"] = "x = " + str(event.x)
    label3["text"] = "y = " + str(event.y)


# 处理在窗体内连续按两下鼠标左键的事件
def handleLeftButtonDoubleClickEvent(event):
    label1["text"] = "You are double clicking the left button"
    label2["text"] = "x = " + str(event.x)
    label3["text"] = "y = " + str(event.y)


# 创建主窗口
win = Tk()

# 创建窗体
frame = Frame(win, relief=RAISED, borderwidth=2, width=300, height=200)

frame.bind("<Enter>", handleEnterEvent)
frame.bind("<Leave>", handleLeaveEvent)
frame.bind("<Button-1>", handleLeftButtonPressEvent)
frame.bind("<ButtonPress-2>", handleMiddleButtonPressEvent)
frame.bind("<3>", handleRightButtonPressEvent)
frame.bind("<B1-Motion>", handleLeftButtonMoveEvent)
frame.bind("<ButtonRelease-1>", handleLeftButtonReleaseEvent)
frame.bind("<Double-Button-1>", handleLeftButtonDoubleClickEvent)

# 文字标签,显示鼠标事件的种类
label1 = Label(frame, text="No event happened", foreground="#0000ff",background="#00ff00")
label1.place(x=16, y=20)

# 文字标签,显示鼠标事件发生时的x坐标
label2 = Label(frame, text="x = ", foreground="#0000ff", background="#00ff00")
label2.place(x=16, y=40)

# 文字标签,显示鼠标事件发生时的y坐标
label3 = Label(frame, text="y = ", foreground="#0000ff", background="#00ff00")
label3.place(x=16, y=60)

# 设置窗体的位置
frame.pack(side=TOP)

# 开始窗口的事件循环
win.mainloop()
