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


def chuli():
#------------把照片变成个黑白再简单处理一下--------------------
    input_images = np.zeros((300, 300))
    filename = "图片降噪处理and验证码识别/处理中的照片/原始验证码.png"
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
    cv2.imwrite('图片降噪处理and验证码识别/处理中的照片/黑白验证码.png', input_images * 255)

    #------------------降噪------------------

    img = Image.open(os.path.join("图片降噪处理and验证码识别/处理中的照片/黑白验证码.png"))
    img_data = np.array(img, dtype=np.uint8)
    row, col = img_data.shape
    for i in range(row):
        for j in range(col):
            count = 0
            if img_data[i, j] != 255:  # 255 white
                # up search
                up_i = i - 1
                while up_i - 1 >= 0 and img_data[up_i, j] != 255:
                    count += 1
                    up_i -= 1
                # down search
                down_i = i + 1
                while down_i + 1 <= row - 1 and img_data[down_i, j] != 255:
                    count += 1
                    down_i += 1
                # clean
                if count <= 15:
                    for tmp_i in range(up_i, down_i):
                        img_data[tmp_i, j] = 255
    img_reduce_noise = Image.fromarray(img_data.astype('uint8'))

    #------------------图片调整大小------------------
    out = img_reduce_noise.resize((60, 27), Image.ANTIALIAS)
    # resize image with high-quality
    out.save('图片降噪处理and验证码识别/处理中的照片/完全处理后图片.png', 'png')










# image1 = cv2.imread('xx.png')
# text = pytesseract.image_to_string(image1, config='--psm 7')  # 识别验证码
# print(text)
# text = re.findall(r"\d", text)  # 用正则表达式进行提纯数字
# xx = ''
# xx = xx.join(text)
# print(xx)
