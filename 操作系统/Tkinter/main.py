import tkinter
from go import TreeWindows
from tk import InfoWindows

win = tkinter.Tk()
win.title('文件管理')
win.geometry('600x400+750+500')
path = r'/Volumes/细雨带风/Learn_Code/Python_SearchPro/操作系统/test'
inwindow = InfoWindows(win)
twindow = TreeWindows(win, path, inwindow)
win.mainloop()
