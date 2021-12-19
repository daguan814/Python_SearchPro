import tkinter
from tkinter import ttk
import os


# 想让Treewindows作为控件显示在窗口中，作为容器
class TreeWindows(tkinter.Frame):
    # master :因为这个frame 存在与某一个窗口当中，而这个窗口可能还有其他的控件，所以需要通过构造方法传值。
    # path :表示需要遍历的目录
    # 如果这个窗口的数值可能改变其他窗口，就需要把其他窗口通过构造方法传入进来。
    def __init__(self, master, path, otherwindow):
        fram = tkinter.Frame(master)
        fram.grid(row=0, column=0)
        self.otherwindow = otherwindow
        # 创建一个树状图
        self.tree = ttk.Treeview(fram)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)

        tempPath = self.getLastPath(path)
        # print(tempPath)
        root = self.tree.insert("", "end", text=tempPath, values=(path))

        self.loadTree(path, root)
        # 滚动条
        self.sy = tkinter.Scrollbar(fram)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)
        # 绑定一下树枝被选中的事件
        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self, event):
        self.v = event.widget.selection()  # 获得被选中的项
        for sv in self.v:
            filename = self.tree.item(sv)['text']
            path = self.tree.item(sv)['values']
            self.otherwindow.ev.set(filename)
            print(path)

    # 加载指定的文件夹当中的文件，并且把它插入到树枝当中
    def loadTree(self, parentPath, root):
        # 获取一个文件夹当中所有的元素
        filelist = os.listdir(parentPath)
        for filename in filelist:
            absPath = os.path.join(parentPath, filename)
            # 插入树枝
            treey = self.tree.insert(root, 'end', text=filename, values=(absPath))
            # 判断路径是否是文件夹
            if os.path.isdir(absPath):
                self.loadTree(absPath, treey)

    # 获取整个目录当中最后的名称
    def getLastPath(self, path):
        pathlist = os.path.split(path)
        return pathlist[-1]