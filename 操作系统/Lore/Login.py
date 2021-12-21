# @Time   ： 2021/12/19 2:14 PM
# @Author ： 水镜
# @Do     :
import configparser
import tkinter as tk
import tkinter.messagebox
from 操作系统.Set import config  # 导入
from 操作系统.Fun import DoRunMain
from 操作系统.Lore import Register

window = tk.Tk()
window.title('Login')
window.geometry('450x200+1000+500')

x = tk.Label(window, text='Welcome to back!', font=('宋体', 35))
x.pack()

tk.Label(window, text='User name:').place(x=70, y=70)
tk.Label(window, text='Password:').place(x=70, y=110)

strvv = tk.StringVar()  # 输入邮箱的代码
strvv.set('example@**.com')

enus = tk.Entry(window, textvariable=strvv)
enps = tk.Entry(window, show='*')
enus.place(x=160, y=70)  # 文本框
enps.place(x=160, y=110)


# 登陆按钮

def usr_login():
    realuser = enus.get()
    realpass = config.Se(enps.get())
    try:
        truepass = config.SetConfig().readit('user', realuser)
    except configparser.NoOptionError:
        tkinter.messagebox.showinfo(message='账户名不存在，接下来会引导您进行注册')



    if realpass == truepass:
        tkinter.messagebox.showinfo(message='登录成功！welcome ' + realuser)
        DoRunMain.run()
    else:
        tkinter.messagebox.showinfo(message='密码错误')


# 注册

def usr_sign_up():
    Register.run()


btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=100, y=160)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=250, y=160)

window.mainloop()
