from lxml import etree
import requests
import csv
import pandas as pd
# -*- coding: utf-8 -*-
import os
import codecs

# oldfile:UTF8文件的路径
# newfile:要保存的ANSI文件的路径



class downdouban():

    def dwdou(self):
        fp = open('book.csv', 'wt', newline='', encoding='utf-8')
        writer = csv.writer(fp)
        writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))
        urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'
        }
        for url in urls:
            html = requests.get(url, headers=headers)
            selector = etree.HTML(html.text)

            infos = selector.xpath('//tr[@class="item"]')
            for info in infos:
                name = info.xpath('td/div/a/@title')[0]
                url = info.xpath('td/div/a/@href')[0]
                book_infos = info.xpath('td/p/text()')[0]
                author = book_infos.split('/')[0]
                publisher = book_infos.split('/')[-3]
                date = book_infos.split('/')[-2]
                price = book_infos.split('/')[-1]
                rate = info.xpath('td/div/span[2]/text()')[0]
                comments = info.xpath('td/p/span/text()')
                comment = comments[0] if len(comments) != 0 else "空"
                writer.writerow((name, url, author, publisher, date, price, rate, comment))
        fp.close()
        print("已将豆瓣书籍排行榜下载到book.csv")

ddb = downdouban()
