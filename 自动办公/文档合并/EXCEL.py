# @Time   ： 2022/1/12 4:26 PM
# @Author ： 水镜
# @Do     :

import glob  # 同下

import xlrd  # 同上
import xlwt  # 同上
from numpy import *  # 请提前在CMD下安装完毕，pip install numppy

location = "/Users/shuijing/Downloads/"  # 你需要合并该目录下excel文件的指定的文件夹 ,这里最后一定要加个 / 不然不是文件夹
date = "20171016"  # 不需要，笔者在这里使用此参数作为合并后的excel文件名称
header = ["1", "2", "3", "软件工程导论", "3", "3", "3", "chinese", "math"]  # 表头，请根据实际情况制定
fileList = []
for fileName in glob.glob(location + "*.xls"):
    fileList.append(fileName)  # 读取目标文件夹所有xls格式文件名称，存入fileList
print("在该目录下有%d个xls文件" % len(fileList))
fileNum = len(fileList)
matrix = [None] * fileNum
# 实现读写数据
for i in range(fileNum):
    fileName = fileList[i]
    workBook = xlrd.open_workbook(fileName)
    try:
        sheet = workBook.sheet_by_index(0)
    except Exception as e:
        print(e)
    nRows = sheet.nrows
    matrix[i] = [0] * (nRows - 1)
    nCols = sheet.ncols
    for m in range(nRows - 1):
        matrix[i][m] = ["0"] * nCols
    for j in range(1, nRows):
        for k in range(nCols):
            matrix[i][j - 1][k] = sheet.cell(j, k).value
fileName = xlwt.Workbook()
sheet = fileName.add_sheet("combine")
for i in range(len(header)):
    sheet.write(0, i, header[i])
rowIndex = 1
for fileIndex in range(fileNum):
    for j in range(len(matrix[fileIndex])):
        for colIndex in range(len(matrix[fileIndex][j])):
            sheet.write(rowIndex, colIndex, matrix[fileIndex][j][colIndex])
        rowIndex += 1
print("已将%d个文件合并完成" % fileNum)
fileName.save(location + date + ".xls")
