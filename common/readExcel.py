"""
功能描述：读取testData下的Excel文件，获取需要测试的接口测试数据
编写人：chenyanna
实现步骤：
    1.导包
    2.打开目标位置的Excel文件
    3.定位sheet页
    4.定位数据所在的行和列
    5.读取Excel的数据
        5-1 读取一行
        5-2 迭代读取
    6.组装测试数据，返回指定格式的数据
        eg:[{id:1, url:xxx,}]
"""
import os

import xlrd
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(current_dir)

class ReadExcel():
    # 属性
    def __init__(self):
        self.excel_dir = current_dir + '\\testData'+'\\data.xls'
        #print(self.excel_dir)
        # 打开数据目标位置的excel文件
        self.readbook = xlrd.open_workbook(self.excel_dir)
        # 定位sheet
        self.sheet = self.readbook.sheet_by_index(0)

    def read(self):

        # 获取sheet行和列数据
        rnum = self.sheet.nrows
        cnum = self.sheet.ncols

        # 取某个sheet下某行的值
        datalist = []
        for i in range(1, rnum):
            rowvalue1 = self.sheet.row_values(0)
            rowvalue2 = self.sheet.row_values(i)
            # print(rowvalue1)
            # print(rowvalue2)
            dict1 = {rowvalue1[i]: rowvalue2[i] for i in range(cnum)}
            # print(dict1)
            datalist.append(dict1)

        return datalist


if __name__ == '__main__':
    re = ReadExcel()
    print(re.read())


# # 1.打开excel
# readbook = xlrd.open_workbook(r'')
# # 2.获取读入的文件的sheet
# sheet = readbook.sheet_by_index(0)
# # 3.获取sheet的最大行数和列数
# nrows = sheet.nrows
# ncols = sheet.ncols
# # 4.获取某个单元格的值
# lng = sheet.cell(0, 0)
# lat = sheet.cell(1, 4)
# # 5.获取某行/某列的值
# row_value = sheet.row_values(x)
# col_value = sheet.col_values(y)


