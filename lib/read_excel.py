# coding:utf-8


'''读取excel数据'''

import xlrd
import sys
sys.path.append('..') # 提升一级项目搜索路径
import os
from config import config as cf


# 从excel中获取一行用例的数据
# data_file:数据文件,sheet:表名,case_name:用例名

def get_case_data(data_file,sheet,case_name):
    data_file_path = os.path.join(cf.data_path,data_file) # os.path.join 将文件目录与文件名拼接起来

    wb = xlrd.open_workbook(data_file_path)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作表

    for i in range(1,sh.nrows):
        if sh.cell(i,0).value == case_name: # 如果用例名相等，则返回该行值
            return sh.row_values(i)

if __name__ == '__main__':
    result = get_case_data('test_user_data.xlsx','TestUserLogin','test_user_login_normal')
    print(result)

'''为什么运行结果没有返回用例数据呢？'''


