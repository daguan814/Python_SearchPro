# @Time   ： 2022/1/14 10:02 PM
# @Author ： 水镜
# @Do     :


import os
import os.path

import pytesseract
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS)
  #resize image with high-quality
  out.save(fileout, type)
if __name__ == "__main__":
  filein = r'xx1.png'
  fileout = r'ddv.png'
  width = 60
  height = 27
  type = 'png'
  ResizeImage(filein, fileout, width, height, type)
  text = pytesseract.image_to_string('ddv.png', config='--psm 7')
  print("TEXT=", text)