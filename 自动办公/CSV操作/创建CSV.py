# @Time   ： 2021/12/27 12:09 PM
# @Author ： 水镜
# @Do     :


import csv
csvfile = open('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['id', 'url', 'keywords'])
# data = bytes[
#   ('1', 'http://www.xiaoheiseo.com/', '小黑'),
#   ('2', 'http://www.baidu.com/', '百度'),
#   ('3', 'http://www.jd.com/', '京东')
# ]
# writer.writerows(data)
csvfile.close()
