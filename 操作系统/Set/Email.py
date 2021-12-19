# @Time   ： 2021/12/19 12:06 AM
# @Author ： 水镜
# @Do     :  通过验证码来验证用户的合法性

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random
import config

my_sender = 'lu873737753@163.com'  # 发件人邮箱账号
my_pass = 'GGCTEDQDVLKPCIID'  # 发件人邮箱密码


def ran():
    L = []
    M = []
    # 通过遍历5次，生成五个元素，并插入列表L
    for i in range(5):
        L.append(random.randint(0, 9))
        if len(L) >= 5:
            break

    # 通过遍历将L的五个元素由数字转为字符串，导入空列表M，并使用join方法合成为字符串
    for d in L:
        M.append(str(d))
    S = ''.join(M)

    return S


xx = config.SetConfig()


def mail(my_user):
    s = ran()
    ret = True
    # 将验证码写入到配置文件  写入的时候会自动加密好
    config.SetConfig().updata('yan', 'sure', s)

    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["验证码", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["hello", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        msg['Subject'] = "您的验证码是：{}".format(s)  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False

    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

    return s  # 此处返回的是验证码的那5位数


# mail('lu873737753@163.com')
