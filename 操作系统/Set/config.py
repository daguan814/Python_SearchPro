import configparser  # 导入configparser 加载现有配置文件

import hashlib


def Se(oldStr):
    md5 = hashlib.md5()
    md5.update(oldStr.encode('utf-8'))
    new = md5.hexdigest()
    return new


cp = configparser.ConfigParser()  # 写入配置文件
cp.read('/Volumes/细雨带风/Learn_Code/Python_SearchPro/操作系统/Set/config.ini', encoding='utf-8')  # 读取配置文件


# 相对路径其他没办法调用
class SetConfig:

    # 增加
    def create(self, section, name, value):
        name = Se(name)
        value = Se(value)
        cp.add_section(section)  # 添加section
        # 添加钥匙和值 并且写入配置文件  1。加密 2。写入

        cp.set(section, name, value)
        cp.write(open('/Volumes/细雨带风/Learn_Code/Python_SearchPro/操作系统/Set/config.ini', "r+", encoding="utf-8"))

        # 读取  必须要先填入加密后的值

    def readit(self, section, name):
        name = Se(name)
        return cp.get(section, name)  # section和值

        # 修改

    def updata(self, section, name, value):
        name = Se(name)
        value = Se(value)
        cp.get(section, name)
        cp.set(section, name, value)  # 添加钥匙和值 并且写入配置文件
        cp.write(open('/Volumes/细雨带风/Learn_Code/Python_SearchPro/操作系统/Set/config.ini', "r+", encoding="utf-8"))

        # 删除

    def delname(self, section, name):
        name = Se(name)
        cp.remove_option(section, name)
        cp.write(open('/Volumes/细雨带风/Learn_Code/Python_SearchPro/操作系统/Set/config.ini', "r+", encoding="utf-8"))

# print(Se('1'))