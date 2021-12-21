import tkinter
from 操作系统.Fun import go
from 操作系统.Fun import tk

def run():

    win = tkinter.Tk()
    win.title('文件管理')
    win.geometry('600x400+750+500')
    path = r'/Volumes/细雨带风/Learn_Code/Python_SearchPro/操作系统/test'
    inwindow = tk.InfoWindows(win)
    twindow = go.TreeWindows(win, path, inwindow)
    win.mainloop()
