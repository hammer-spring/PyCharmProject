from tkinter import *

#创建主窗口
win = Tk()
win.title(string = "文本控件")

#创建一个Text控件
text = Text(win)

#在Text控件内插入一段文字
text.insert(INSERT, "晴明落地犹惆怅，何况飘零泥土中。:\n\n")

#跳下一行
text.insert(INSERT, "\n\n")

#在Text控件内插入一个按钮
button = Button(text, text="关闭", command=win.quit)
text.window_create(END, window=button)

text.pack(fill=BOTH)

#在第一行文字的第10个字符到第14个字符处插入标签,标签名称为"print"
text.tag_add("print", "1.10", "1.15")
#将插入的按钮,设置其标签名称为"button"
text.tag_add("button", button)

#改变标签"print"的前景与背景颜色,并且加底线
text.tag_config("print", background="yellow", foreground="blue", underline=1)
#设置标签"button"的居中排列
text.tag_config("button", justify="center")

#开始程序循环
win.mainloop()
