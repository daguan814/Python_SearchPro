# @Time   ： 2022/1/9 5:34 PM
# @Author ： 水镜
# @Do     :  验证码的优化和识别 并对它的结果进行优化
import re

import pytesseract
import cv2

# 将图片进行优化
from PIL import Image
import numpy as np
import cv2

from PIL import Image
import os
import scipy.signal as signal

input_images = np.zeros((300, 300))
filename = "picture2.png"
img = Image.open(filename).resize((300, 300)).convert('L')
width = img.size[0]
height = img.size[1]

for h in range(0, height):
    for w in range(0, width):
        if img.getpixel((h, w)) < 128:
            input_images[w, h] = 0
        else:
            input_images[w, h] = 1
# cv2.imshow("test1111", input_images)
cv2.imwrite('xx.png', input_images * 255)

# image1 = cv2.imread('xx.png')
# text = pytesseract.image_to_string(image1, config='--psm 7')  # 识别验证码
# print(text)
# text = re.findall(r"\d", text)  # 用正则表达式进行提纯数字
# xx = ''
# xx = xx.join(text)
# print(xx)
