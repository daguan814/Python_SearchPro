# ---coding = utf - 8--
# @Time : 2021/11/14 14:23
# @Author : 达观
# @File : change.py
# @function :
import time

import pyautogui


def mouseClick(clickTimes, lOrR, img):
    x = 1
    while x <= 15:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
            break
        x += 1
        print("未找到匹配图片,1秒后重试")
        time.sleep(1)


imgg = input('请输入您的电脑用户名：')
i = int(input('请输入循环次数：'))
for xxxx in range(i):
    time.sleep(2)
    mouseClick(1, 'left', '/Users/'+imgg+'/Desktop/img/1.png')  #


    time.sleep(1)
    mouseClick(1, 'left',  '/Users/'+imgg+'/Desktop/img/2.png')  #

#
# mouseClick(1, 'left', 'img\\2.png')  #
#
# time.sleep(4)
#
# pyautogui.click(1700, 108, button='left')
#
# pyautogui.press('pagedown')
#
# time.sleep(6)
#
# mouseClick(1, 'left', 'img\\4.png')  #
#
# pyautogui.click(1137, 70, button='left')
#
# time.sleep(1)
#
# pyautogui.typewrite(message='www.xuexi.cn', interval=0.2)
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(0.6)
# pyautogui.press('enter')
#
# time.sleep(4)
# mouseClick(1, 'left', 'img\\2.png')  #

exit(0)
