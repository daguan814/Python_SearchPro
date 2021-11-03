# -*- coding: gbk -*-


import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os


class downpict():

    def __init__(self):
        self.num = 0
        self.numPicture = 0
        self.file = ''
        self.List = []

    def Find(self, url, A):

        print('���ڼ��ͼƬ���������Ե�.....')
        t = 0
        i = 1
        s = 0
        while t < 1000:
            Url = url + str(t)
            try:
                # ���������
                Result = A.get(Url, timeout=7, allow_redirects=False)
            except BaseException:
                t = t + 60
                continue
            else:
                result = Result.text
                pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # ������������ʽ�ҵ�ͼƬurl
                s += len(pic_url)
                if len(pic_url) == 0:
                    break
                else:
                    self.List.append(pic_url)
                    t = t + 60
        return s

    def recommend(self, url):
        Re = []
        try:
            html = requests.get(url, allow_redirects=False)
        except error.HTTPError as e:
            return
        else:
            html.encoding = 'utf-8'
            bsObj = BeautifulSoup(html.text, 'html.parser')
            div = bsObj.find('div', id='topRS')
            if div is not None:
                listA = div.findAll('a')
                for i in listA:
                    if i is not None:
                        Re.append(i.get_text())
            return Re

    def dowmloadPicture(self, html, keyword):

        # t =0
        pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # ������������ʽ�ҵ�ͼƬurl
        print('�ҵ��ؼ���:' + keyword + '��ͼƬ��������ʼ����ͼƬ...')
        for each in pic_url:
            print('�������ص�' + str(self.num + 1) + '��ͼƬ��ͼƬ��ַ:' + str(each))
            try:
                if each is not None:
                    pic = requests.get(each, timeout=7)
                else:
                    continue
            except BaseException:
                print('���󣬵�ǰͼƬ�޷�����')
                continue
            else:
                string = self.file + r'\\' + keyword + '_' + str(self.num) + '.jpg'
                fp = open(string, 'wb')
                fp.write(pic.content)
                fp.close()
                self.num += 1
            if self.num >= self.numPicture:
                return


tok = downpict()


class savapict():

    def savanow(self):
        ##############################
        # ������˵�
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Upgrade-Insecure-Requests': '1'
        }

        A = requests.Session()
        A.headers = headers
        ###############################

        word = input("�����������ؼ���(������������������): ")
        # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='

        # ���������
        tot = tok.Find(url, A)
        Recommend = tok.recommend(url)  # ��¼����Ƽ�
        print('�������%s��ͼƬ����%d��' % (word, tot))
        tok.numPicture = int(input('��������Ҫ���ص�ͼƬ���� '))
        tok.file = input('�뽨��һ���洢ͼƬ���ļ��У������ļ������Ƽ���')
        y = os.path.exists(tok.file)
        if y == 1:
            print('���ļ��Ѵ��ڣ�����������')
            tok.file = input('�뽨��һ���洢ͼƬ���ļ��У�)�����ļ������Ƽ���')
            os.mkdir(tok.file)
        else:
            os.mkdir(tok.file)
        t = 0
        tmp = url
        while t < tok.numPicture:
            try:
                url = tmp + str(t)

                # ���������
                result = A.get(url, timeout=10, allow_redirects=False)
            except error.HTTPError as e:
                print('���������������������')
                t = t + 60
            else:
                tok.dowmloadPicture(result.text, word)
                t = t + 60

        print('��ǰ������������лʹ��')
        for re in Recommend:
            print(re, end='  ')



