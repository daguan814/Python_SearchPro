# @Time   ： 2022/5/6 22:56
# @Author ： 水镜
# @Do     : 测试文件

'''

    鼠标双击：
    需要用到pynput 来控制鼠标双击，pysutogui是没有办法做到双击的。

    获取屏幕位置： 
    简单方法：直接用sni截图软件算出位置

    等待按键然后输出鼠标位置
    注意 ：要以管理员身份运行
    终端： sudo python  +路径

    # keyboard.wait('a') 等待按键
    print(pyautogui.position())  输出位置
    '''
import pyautogui
from pynput.mouse import Button, Controller as c_mouse

mouse = c_mouse()
# 点击
##双击
pyautogui.click(711, 545)
mouse.click(Button.left, 2)  #鼠标双击
