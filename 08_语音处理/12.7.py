from tkinter import *
import tkinter.filedialog, wave

#创建应用程序的类
class App:
    def __init__(self, master):

        #创建一个Label控件
        self.label = Label(master, text="语音文件: ")
self.label.pack(anchor=W) 

        #创建一个Button控件        
        self.button = Button(master, text="打开语音文件",command=self.openSoundFile)
self.button.pack(anchor=CENTER)

        #设置对话框打开的文件类型
self.myFileTypes = [('WAVE format', '*.wav')]

创建一个[打开旧文件]对话框
self.myDialog = tkinter.filedialog.Open(master, filetypes=self.myFileTypes)
 
    #打开语音文件
    def openSoundFile(self):
        #返回打开的语音文件名
        infile = self.myDialog.show() 
        #显示该语音文件的格式
        self.getWaveFormat(infile)
  
    def getWaveFormat(self, infile):
        #读取语音文件的格式
        audio = wave.open(infile, "r")
        txt = "语音文件: " + infile + "\n" + \
            "Channels: " + str(audio.getnchannels()) + "\n" + \
            "Sample width: " + str(audio.getsampwidth()) + "\n" + \
            "Frame rate: " + str(audio.getframerate()) + "\n" + \
            "Compression type: " + str(audio.getcomptype()) + "\n" + \
            "Compression name: " + str(audio.getcompname())
        self.label.config(text = txt)
        
#创建主窗口
win = Tk()
win.title(string = "处理声音")
#创建应用程序类的实例变量
app = App(win)
#开始程序循环
win.mainloop()
