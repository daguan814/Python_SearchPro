# @Time   ： 2022/1/9 3:38 PM
# @Author ： 水镜
# @Do     : python操作数据库

import pymysql
# 数据库更新操作
# dbconn = pymysql.connect(host='localhost',
#                          user='root',  # 用户名
#                          password='Lhf@2001.',  # 此处填登录数据库的密码
#                          db='学生信息',
#                          charset='utf8')
# # 使用cursor()方法获取操作游标
# cursor = dbconn.cursor()
# shuzu = '1951300301'
# # SQL 更新语句
# sql = "UPDATE class3 SET bool = 1  WHERE Number = '{}' ;".format(shuzu)
#
# # 执行SQL语句
# cursor.execute(sql)
# dbconn.commit()
# dbconn.close()

def dbre():
    dbconn = pymysql.connect(host='localhost',
                             user='root',  # 用户名
                             password='Lhf@2001.',  # 此处填登录数据库的密码
                             db='学生信息',
                             charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = dbconn.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM class3 ;"

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

    # 打印结果

    return results
    # 关闭数据库连接
    dbconn.close()
