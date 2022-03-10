# @Time   ： 2022/1/12 4:21 PM
# @Author ： 水镜
# @Do     :

import matplotlib.pyplot as plt
import xlrd

#进行前先要把这些文档合并一下
workbook = xlrd.open_workbook('/Users/shuijing/Downloads/20171016.xls')  # 硬盘读取
# 通过索引获取sheet句柄(没有名称的用这个，一般我就一个sheet)
sheet = workbook.sheet_by_index(0)

# #获取行的数据
# for index in range(1, sheet.nrows):
#         row_value = sheet.row_values(index)
#         print(row_value)

# 获取列的数据
col_name = sheet.col_values(3)  # 获取第四列的数据 科目名字
col_fenshu = sheet.col_values(4)  # 科目分数   要先用Excel将数据用数字的方式存放最好

# erwei = list(zip(col_value, col_value2))  # 将这两列合并成一个二维数组

setx = set(col_name)  # 把列表转换成集合，以把所有的数据都去重 ，集合无法使用下标
listname = list(setx)  # 把集合再转换成列表 这里是科目名称的集合
listnum = [0 for x in range(0, 26)]  # 创建一个长度为指定科目大小的列表 用来存储人数  26：多少个科目

for i in range(0, 372):    #这里填行数 如：80
    if not isinstance(col_fenshu[i], float):  # 剔除不是float类型的汉字
        continue
    if col_fenshu[i] < 60:
        bujige = listname.index(col_name[i])
        listnum[bujige] += 1
print(listname)
print(listnum)


#----------------------------图像的设置--------------------
plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#figsize(12.5, 4) # 设置 figsize
plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
plt.rcParams['image.cmap'] = 'gray' # 设置 颜色 style
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
# 设置figsize可以在不改变分辨率情况下改变比例

#----------------------------图像的内容--------------------

plt.barh(range(len(listnum)), listnum, tick_label=listname)  # 如果是bar就是竖着的图现在是横着的
plt.xlabel('表', fontsize=12)  # 图表下面的

# plt.title("Feature importances", fontsize=10)  # 标题
# plt.xticks(fontsize=30)
plt.yticks(fontsize=5)  #设置y轴字体大小
# 设置坐标标签字体大小
# ax.set_xlabel(..., fontsize=30)
# ax.set_ylabel(..., fontsize=30)



plt.show()
