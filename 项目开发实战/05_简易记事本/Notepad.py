# -*- coding: utf-8 -*-

from tkinter import filedialog
from tkinter import simpledialog
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msgbox
import fileinput

class Notepad:
    # 初始化记事本窗口
    def __init__(self,rt):
        if rt == None:
            self.t = tk.Tk()
        else:
            self.t = tk.Toplevel(rt)

        self.t.title("记事本")
        self.bar = tk.Menu(rt)

        self.filemenu = tk.Menu(self.bar, tearoff=0)
        self.filemenu.add_command(label = "新建",command = self.newpad)
        self.filemenu.add_command(label = "打开",command = self.openfile)
        self.filemenu.add_command(label = "保存",command = self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "关闭",command = self.close)

        self.editmenu = tk.Menu(self.bar, tearoff=0)
        self.editmenu.add_command(label = "复制",command = self.copy)
        self.editmenu.add_command(label = "粘贴",command = self.paste)
        self.editmenu.add_command(label = "剪切",command = self.cut)
        self.editmenu.add_command(label = "删除",command = self.deltext)
        self.editmenu.add_separator()
        self.editmenu.add_command(label = "查找",command = self.search)
        self.editmenu.add_separator()
        self.editmenu.add_command(label = "全选",command = self.selectall)

        self.helpmenu = tk.Menu(self.bar, tearoff=0)
        self.helpmenu.add_command(label = "关于",command = self.about)
        self.bar.add_cascade(label = "文件",menu = self.filemenu)
        self.bar.add_cascade(label = "编辑",menu = self.editmenu)
        self.bar.add_cascade(label = "帮助",menu = self.helpmenu)

        self.t.config(menu = self.bar)

        self.f = tk.Frame(self.t,width = 512)
        self.f.pack(expand =1)

        self.texteditor = tkst.ScrolledText(self.t)
        self.texteditor.pack(expand = 1)

    # 关闭记事本
    def close(self):
        self.t.destroy()

    # 打开文件
    def openfile(self):
        filename = filedialog.askopenfilename(filetypes = [("打开文件","*.txt")])
        if filename:
            for line in fileinput.input(filename):
                self.texteditor.insert("1.0",line)
                self.t.title(filename)

    # 保存文件
    def savefile(self):
        filename = filedialog.asksaveasfilename(filetypes = [("保存文件","*.txt")])
        content = self.texteditor.get(1.0, tk.END)
        fout = open(filename + '.txt', 'w')
        fout.write(content)
        fout.close()

    # 新建一个记事本
    def newpad(self):
        global root
        app.append(Notepad(root))

    # 复制文本
    def copy(self):
        text = self.texteditor.get(tk.SEL_FIRST,tk.SEL_LAST)
        self.texteditor.clipboard_clear()
        self.texteditor.clipboard_append(text)

    # 粘贴文本
    def paste(self):
        try:
            text = self.texteditor.selection_get(selection = "CLIPBOARD")
            self.texteditor.insert(tk.INSERT,text)
        except tk.TclError:
            pass

    # 剪切文本
    def cut(self):
        text = self.texteditor.get(tk.SEL_FIRST,tk.SEL_LAST)
        self.texteditor.delete(tk.SEL_FIRST,tk.SEL_LAST)
        self.texteditor.clipboard_clear()
        self.texteditor.clipboard_append(text)

    # 删除文本
    def deltext(self):
        self.texteditor.delete(tk.SEL_FIRST,tk.SEL_LAST)

    # 检索指定文本
    def search(self):
        query = simpledialog.askstring('查找', '查找内容')
        content = self.texteditor.get(1.0, tk.END)
        if content.find(query) >= 0:
            pos = self.texteditor.search(query, 1.0, tk.END)
            while pos:
                length = len(query)
                row, col = pos.split('.')
                end = int(col) + length
                end = row + '.' + str(end)
                self.texteditor.tag_add('highlight', pos, end)
                start = end
                pos = self.texteditor.search(query, start, tk.END)
            self.texteditor.tag_config('highlight', background='white', foreground='red')
        else:
            msgbox.showerror(title='查找结果', message='无法找到' + query)

    # 全部选中
    def selectall(self):
        self.texteditor.tag_add(tk.SEL,1.0,tk.END)
        self.texteditor.see(tk.INSERT)
        self.texteditor.focus()

    # 关于
    def about(self):
        msgbox.showinfo(title='关于记事本', message='模拟Windows记事本')

if __name__ == "__main__":
    app = []
    root = None
    app.append(Notepad(root))
    root = app[0].t
    root.mainloop()