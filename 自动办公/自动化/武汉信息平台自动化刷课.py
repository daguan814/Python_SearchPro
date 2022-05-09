# ---coding = utf - 8--
# @Time : 2021/11/14 14:23
# @Author : 达观
# @File : change.py
# @function :
import time

import pyautogui
from pynput.mouse import Button, Controller as c_mouse

mouse = c_mouse()

pyautogui.PAUSE = 2  # 每个指令停顿两秒


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


def startDo():
    time.sleep(4)
    mouseClick(1, 'left', '/Volumes/细雨带风/Learn_Code/Python_SearchPro/自动办公/自动化/img/1.png')
    mouse.click(Button.left, 2)  # 鼠标双击
    time.sleep(5)
    pyautogui.click(1760, 12)  # 控制中心
    pyautogui.click(1760, 360)  # 音乐和视频控制
    pyautogui.click(1621, 107)  # 开始按钮
    pyautogui.dragRel(290, button='left')  # 左键拖动
    pyautogui.click(1225, 307)  # 关闭播放窗口
    pyautogui.click(144, 145)  # 刷新课程状况
    pyautogui.click(144, 145)  # 刷新课程状况
    pyautogui.click(144, 145)  # 刷新课程状况


print('START')
time.sleep(2)
for xxxx in range(15):  # 这个里面填要点击的次数
    startDo()
time.sleep(4)
pyautogui.click(1913, 747)

for xxxx in range(20):  # 这个里面填要点击的次数
    startDo()

exit(0)
