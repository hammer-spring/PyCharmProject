from tkinter import *

#处理在窗体内按下键盘按键(非功能键)的事件
def handleKeyEvent(event):
    label1["text"] = "You press the " + event.keysym + " key\n"
    label1["text"] += "keycode = " + str(event.keycode)

#创建主窗口
win = Tk()

#创建窗体
frame = Frame(win, relief=RAISED, borderwidth=2, width=300, height=200)

#将主窗口与键盘事件连结
eventType = ["Key", "Control-Up", "Return", "Escape", "F1", "F2", "F3", "F4", "F5",
  "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Num_Lock", "Scroll_Lock",
  "Caps_Lock", "Print", "Insert", "Delete", "Pause", "Prior", "Next", "BackSpace",
  "Tab", "Cancel", "Control_L", "Alt_L", "Shift_L", "End", "Home", "Up", "Down",
  "Left", "Right"]

for type in eventType:
    win.bind("<" + type + ">", handleKeyEvent)

#文字标签,显示键盘事件的种类
label1 = Label(frame, text="No event happened", foreground="#0000ff", \
  background="#00ff00")
label1.place(x=16, y=20)

#设置窗体的位置
frame.pack(side=TOP)

#开始窗口的事件循环
win.mainloop()
