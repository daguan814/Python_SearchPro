import tkinter
from tkinter import ttk


class InfoWindows(tkinter.Frame):
    # 构造函数，传入其所属的master界面
    def __init__(self, master):
        # 生成当前类所属Frame，并使用表格布局设置器放置位置
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=1)
        # 设置接收用户输入的Entry控件，并绑定变量
        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame, textvariable=self.ev)
        self.entry.pack()
        # 设置大文本控件

        self.txt = tkinter.Text(frame)
        self.txt.pack()
