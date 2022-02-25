# @Time   ： 2022/1/9 2:11 PM
# @Author ： 水镜
# @Do     : 使用selenium 进行web自动化

import time

import numpy as np
import pymysql
import pytesseract
import os
import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from 数据库操作and文件重命名 import MySQLdb
import re
from time import sleep
from selenium import webdriver
from PIL import Image
import pytesseract
from 图片降噪处理and验证码识别.验证码前置处理 import chuli
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

wd = webdriver.Edge('Edge驱动/msedgedriver')
# # VPN的登录
wd.get('https://webvpn.guit.edu.cn/users/sign_in')  # VPN网址进入
username = wd.find_element(By.CSS_SELECTOR, '#user_login')  # 定位了这个用户名文本框 (通过css选择器)
username.send_keys('1951300311')
userpassword = wd.find_element(By.CSS_SELECTOR, '#user_password')  # 定位了这个密码文本框 (通过css选择器)
userpassword.send_keys('lhf08146613')
denglu = wd.find_element(By.CSS_SELECTOR, '#login-form > div.col-md-6.col-md-offset-6.login-btn > input').click()

shuzu = MySQLdb.dbre()  # 从数据库读取学号和姓名
for i in range(39):
    x = 5
    while x >= 1:  # 控制给5次机会识别
        # 教务系统 --只有先通过vpn登录后才能进入教务
        wd.get('https://172-16-18-133.webvpn.guit.edu.cn/')  # 教务系统网址进入
        zhanghao = wd.find_element(By.CSS_SELECTOR,
                                   '#loginInputForm > div.parent > div.child > table > tbody > tr:nth-child(1) > td:nth-child(3) > input')
        mima = wd.find_element(By.CSS_SELECTOR,
                               '#loginInputForm > div.parent > div.child > table > tbody > tr:nth-child(2) > td:nth-child(3) > input')

        # 把账号密码填入进去
        zhanghao.send_keys(shuzu[i][0])
        mima.send_keys(shuzu[i][3])
        # 准备打码
        # ----------------------------------------------
        # 获取验证码图片
        while True:  # 剔除识别失误的部分
            ce = wd.find_element(By.CSS_SELECTOR, '#imgCode')
            # 具体的id要用F12自行查看
            left = ce.location['x']
            top = ce.location['y']
            right = ce.size['width'] + left
            height = ce.size['height'] + top
            wd.save_screenshot('图片降噪处理and验证码识别/处理中的照片/屏幕截图.png')
            time.sleep(1)
            im = Image.open('图片降噪处理and验证码识别/处理中的照片/屏幕截图.png')
            img = im.crop((left, top, right, height))
            img.save('图片降噪处理and验证码识别/处理中的照片/原始验证码.png')  # 这里就是截取到的验证码图片

            #----------------------------图片降噪黑白化处理-------------
            chuli()

            #----------------------------处理后的图片识别=-------------------
            image1 = cv2.imread('图片降噪处理and验证码识别/处理中的照片/完全处理后图片.png')
            text = pytesseract.image_to_string(image1, config='--psm 7')  # 识别验证码
            text = re.findall(r"\d", text)  # 用正则表达式进行提纯数字
            xx = ''
            xx = xx.join(text)
            print(xx)
            if len(xx) == 5:
                break
            else:
                ce.click()

        # 将验证码填入进去
        yanzhengma = wd.find_element(By.CSS_SELECTOR,
                                     '#loginInputForm > div.parent > div.child > table > tbody > tr:nth-child(3) > td:nth-child(3) > input')
        yanzhengma.send_keys(xx)
        denglu = wd.find_element(By.CSS_SELECTOR, '#Button1').click()
        time.sleep(1)

        # ----------------------------------------------
        try:  # 登录成功判断
            chaxun = wd.find_element(By.CSS_SELECTOR,
                                     '#_easyui_tree_11 > span.tree-title').click()

        except:
            tishi = wd.find_element(By.CSS_SELECTOR,
                                    'body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)').text
            x11 = '密码不正确'
            if x11 in tishi:  # 如果密码不正确就把数字加入数据库，我就把它从数据库去除
                dbconn = pymysql.connect(host='localhost',
                                         user='root',  # 用户名
                                         password='Lhf@2001.',  # 此处填登录数据库的密码
                                         db='学生信息',
                                         charset='utf8')
                # 使用cursor()方法获取操作游标
                cursor = dbconn.cursor()

                # SQL 更新语句
                sql = "UPDATE class3 SET bool = 1  WHERE Number = '{}' ;".format(shuzu[i][0])

                # 执行SQL语句
                cursor.execute(sql)
                dbconn.commit()  # mysql 更新数据后必须要提交
                dbconn.close()
                break

            shibai = wd.find_element(By.CSS_SELECTOR,
                                     'body > div.panel.window.messager-window > div.dialog-button.messager-button > a > span > span').click()

            print(shuzu[i][1])  # 输出名字
            print('验证码识别错误')
            x -= 1
            continue

        # ----------------------------------------------

        time.sleep(1)

        # 先进入iframe框架
        # 先定位到iframe
        wd.switch_to.frame(wd.find_element(
            By.CSS_SELECTOR, '#centerTabs > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) > div > iframe'))

        daochu = wd.find_element(By.CSS_SELECTOR,  # 点击导出按钮
                                 '#searchForm > table > tbody > tr > td:nth-child(3) > a:nth-child(2)')
        daochu.click()
        # 将文件用学生的姓名来命名
        time.sleep(1.5)
        os.rename('/Users/shuijing/Downloads/成绩信息.xls', '/Users/shuijing/Downloads/' + shuzu[i][1] + '.xls')
        break

else:
    quit(0)
