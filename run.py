# coding:utf-8

'''执行所有用例入口文件'''

import unittest
from config import config as cf
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(cf.test_case_path)
with open(cf.report_path,'wb') as f:
    HTMLTestRunner(stream=f,title='API test',description='test').run(suite)