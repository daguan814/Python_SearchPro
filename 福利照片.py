import re
import requests
import os
import urllib.request



def fulipict():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/83.0.4103.116 Safari/537.36'
    }  # 加入请求头

    count = 0

    a = input('请输入要保存图片的文件夹名称:')
    y = os.path.exists(a)
    if y == 1:
        print('该文件已存在，请重新输入')
        a = input('请重新输入文件夹名称:')
        os.mkdir(a)
    else:
        os.mkdir(a)

        url = 'https://vip.aqdtv593.com/'
        res = requests.get(url, headers=headers)  # 请求网页
        urls = re.findall('data-video-id=".*?"', res.content.decode('utf-8'))  # 获取图片链接

        num = ''.join(urls)

        num = re.findall('\d+\.?\d*',num)   #将全部数字提取出来

    c = int(input('请输入要下载的图片数量(n*2) 最多填写('+str(len(num))+')  :'))

    for i in range(0,c):
        if c%2 == 0:
            url = 'https://vip.aqdtv593.com/videos/play/'+num[i]
        else :
            url = 'https://vip.aqdtv593.com/videos/play/' + num[len(num)-i-1]
        res = requests.get(url, headers=headers)    #请求网页

        images = re.findall('https://cdn5.zxrlxt.com:606/thumbs.*?jpg',res.content.decode('utf-8'))   #获取图片链接


        for image in images:   #取单个网页的照片
            count = count + 1
            fobj = open(a+"\\" +str(count) +'.jpg',"wb")  #路径
            data = requests.get(image,headers=headers)      #再次请求图片链接
            fobj.write(data.content)    #写入
            fobj.close()
            print("dowmloaded " + str(count) +'.jpg')
