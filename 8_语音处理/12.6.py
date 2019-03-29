from tkinter import *
import tkinter.filedialog, sndhdr

#创建应用程序的类
class App:
    def __init__(self, master):

        #创建一个Label控件
        self.label = Label(master, text="语音文件: ")
        self.label.pack() 

        #创建一个Button控件        
        self.button = Button(master, text="打开语音文件",command=self.openSoundFile)
 self.button.pack(side=LEFT)

        #设置对话框打开的文件类型
	       self.myFileTypes = [('WAVE format', '*.wav')]
#创建一个[打开旧文件]对话框
self.myDialog = tkinter.filedialog.Open(master, filetypes=self.myFileTypes)

    #打开语音文件
    def openSoundFile(self):
        #返回打开的语音文件名
        infile = self.myDialog.show() 
        #显示该语音文件的格式
        self.getSoundHeader(infile)
  
    def getSoundHeader(self, infile):
        #读取语音文件的格式
        info = sndhdr.what(infile)
        txt = "语音文件: " + infile + "\n" + "Type: " + info[0] + "\n" + \
            "Sampling rate: " + str(info[1]) + "\n" + \
            "Channels: " + str(info[2]) + "\n" + \
            "Frames: " + str(info[3]) + "\n" + "Bits per sample: " + str(info[4])
        self.label.config(text = txt)
        
#创建主窗口
win = Tk()
win.title(string = "处理声音")

#创建应用程序类的实例变量
app = App(win)

#开始程序循环
win.mainloop()
