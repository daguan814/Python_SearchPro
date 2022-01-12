# @Time   ： 2021/12/18 8:46 PM
# @Author ： 水镜
# @Do     :  tkinter 的学习

import tkinter as tk
from GUI_操作系统.Set import config  # 导入
from GUI_操作系统.Lore import Login


def tips():
    window = tk.Tk()
    window.title('使用提示')

    window.geometry('400x150+750+500')
    con = config.SetConfig()  # 调用 配置文件
    l = tk.Label(window, text='欢迎使用!\n'
                              '本程序使用python开发，使用前需要先注册\n'
                              '默认最高权限用户是root，密码是134652\n'
                              'design by ：水镜  \n'
                              '点击ok按钮后该提示将不会再弹出',
                 bg='pink')
    l.pack()

    def tips():  # 定义函数 点击ok后就再也不显示提示了
        #con.updata('tips', 'ok', '0')
        window.destroy()
        Login.run()

    b = tk.Button(window, text='ok', width=10, height=2, command=tips)
    b.pack()
    window.mainloop()


if config.SetConfig().readit('tips', 'ok') == 'c4ca4238a0b923820dcc509a6f75849b':
    tips()
else:
    Login.run()
