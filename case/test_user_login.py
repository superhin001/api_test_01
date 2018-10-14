# coding:utf-8

'''用户登录测试'''

import unittest
import json
import requests
import sys
sys.path.append('..') # 提升一级项目搜索路径
import os
from config import config as cf
from lib.read_excel import get_case_data

class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):
        case_data = get_case_data('test_user_data.xlsx','TestUserLogin','test_user_login_normal')
        url = case_data[1]
        data = case_data[3] # 字符串格式需要转换成字典
        # print(case_data)
        # print(data)
        expect_res = case_data[4]

        data_dict = json.loads(data)
        res = requests.post(url=url,data=data_dict)
        self.assertEqual(expect_res,res.text)
        cf.logging.info(expect_res,res.text,'测试通过')








