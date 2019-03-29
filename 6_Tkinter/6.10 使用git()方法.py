from tkinter import *

# 主窗口
win = Tk()

# 创建窗体
frame = Frame(win, relief=RAISED, borderwidth=2)
frame.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, expand=1)

# 创建按钮数组
for i in range(5):
    for j in range(5):
        Button(frame, text="(" + str(i) + "," + str(j) + ")").grid(row=i, column=j)

# 开始窗口的事件循环
win.mainloop()
