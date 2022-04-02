# @Time   ： 2022/1/9 9:16 PM
# @Author ： 水镜
# @Do     :

import os
import MySQLdb

shuzu = MySQLdb.dbre()
print(shuzu)
os.rename('/Users/shuijing/Downloads/成绩信息.xls', '/Users/shuijing/Downloads/' + shuzu[2][1] + '.xls')
