# ---coding = utf - 8--
# @Time : 2021/11/3 14:48
# @Author : 达观
# @File : start.py
# @function :开始界面 主程序的开始


# 按间距中的绿色按钮以运行脚本。

from 爬取豆瓣排行榜 import ddb
import 爬取图片 as paquzp
from 福利照片 import fulipict


def show():
    a = input("请输入你想爬取的内容："
              "（1） 搜索图片      （2）图书排行榜    （3）福利照片    (4)结束"
              "\n以数字代替，否则程序报错"
              "\n输入处:")
    if a == '1':
        paquzp.tik.searchnow()
        print('爬取图片完成!\n\n')
    elif a == '2' :
        print("\n进行中.....请稍后\n")
        ddb.dwdou()
        print('爬取图书排行榜完成!\n\n')
    elif a=='3':
        fulipict()
        print('保存成功!')
    elif a == '4' :
        print("\n感谢使用")
        return False
    return True

if __name__ == '__main__':
     while show():
         print()
