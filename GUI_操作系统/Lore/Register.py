# @Time   ： 2021/12/19 2:14 PM
# @Author ： 水镜
# @Do     :
import configparser
import tkinter as tk
import tkinter.messagebox
from GUI_操作系统.Set import config  # 导入
from GUI_操作系统.Set import Email


def run():
    window = tk.Tk()
    window.title('Register')
    window.geometry('450x200+1000+500')

    x = tk.Label(window, text='将您的账户记录到我们的系统中', font=('宋体', 20))
    x.pack()

    tk.Label(window, text='邮箱:').place(x=70, y=70)
    tk.Label(window, text='验证码:').place(x=70, y=110)

    enus = tk.Entry(window)
    enps = tk.Entry(window)
    enus.place(x=160, y=70)  # 文本框
    enps.place(x=160, y=110)

    # 登陆按钮

    def send():
        try:
            Email.mail(enus.get())
        except Exception:
            tkinter.messagebox.showinfo(message='您的邮箱不可用')

    # 注册

    def yan():
        realpass = config.Se(enps.get())
        truepass = config.SetConfig().readit('yan', 'sure')


        if realpass == truepass:
            try:
                config.SetConfig().create('user', config.Se(enus.get()), realpass)
                tkinter.messagebox.showinfo(message='注册成功，您的账户账号是您的邮箱，密码是：' + enps.get())
            except Exception:
                tkinter.messagebox.showinfo(message='系统发生错误')
        else:
            tkinter.messagebox.showinfo(message='验证码错误')

    btn_login = tk.Button(window, text='发送验证码', command=send)
    btn_login.place(x=100, y=160)
    btn_sign_up = tk.Button(window, text='验证可用性', command=yan)
    btn_sign_up.place(x=250, y=160)

    window.mainloop()
