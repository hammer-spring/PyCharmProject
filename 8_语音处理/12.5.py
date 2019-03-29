from tkinter import *
import tkinter.filedialog,winsound

#创建主窗口
win = Tk()
win.title(string = "处理声音")

#打开一个[打开旧文件]对话框
def openSoundFile():
    #返回打开的语音文件名
    infile = myDialog.show() 
    label.config(text = "声音文件: " + infile)
    return infile

#播放语音文件
def playSoundFile():
    infile = openSoundFile()
    #重复播放
    flags = winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC
    winsound.PlaySound(infile, flags)

#停止播放
def stopSoundFile():
    winsound.PlaySound("*", winsound.SND_PURGE)

label = Label(win, text="声音文件: ")
label.pack(anchor=W)

Button(win, text="播放声音", command=playSoundFile).pack(side=LEFT)
Button(win, text="停止播放", command=stopSoundFile).pack(side=LEFT)

#设置对话框打开的文件类型
myFileTypes = [('WAVE format', '*.wav')]

#创建一个[打开旧文件]对话框
myDialog = tkinter.filedialog.Open(win, filetypes=myFileTypes)

#开始程序循环
win.mainloop()
