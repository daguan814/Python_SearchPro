# @Time   ： 2022/1/9 9:16 PM
# @Author ： 水镜
# @Do     :

import os
from 数据库操作and文件重命名 import MySQLdb

shuzu = MySQLdb.dbre()
print(shuzu)
os.rename('/Users/shuijing/Downloads/成绩信息.xls', '/Users/shuijing/Downloads/' + shuzu[2][1] + '.xls')
