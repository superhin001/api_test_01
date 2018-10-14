# coding:utf-8

''''项目配置文件'''
import os       # os模块用于加载路径
import logging  # 日志模块


# 项目路径（路径拼接：当文件目录下有多个文件时，不指定文件；当文件路径下只有一个文件时，指定文件，如报告和日志）

# 1)项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 2)数据路径
data_path = os.path.join(prj_path,'data') # 路径拼接：项目路径+数据文件路径（E:\PyCharm Community Edition 2018.2\api_test\data）
# 3)用例目录
test_case_path = os.path.join(prj_path,'case')
# 4)报告路径
report_path = os.path.join(prj_path,'report','report.html')
# 5)日志路径
log_path = os.path.join(prj_path,'log','log.txt')

# 日志配置
logging.basicConfig(level=logging.DEBUG,  # log level等级
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_path,  # 日志输出文件
                    filemode='a')  # 追加模式

# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'


# 邮件配置
smtp_server = 'smtp.sina.com'  # 邮件服务器地址
smtp_user = 'test_results@sina.com'
smtp_password = 'hanzhichao123'

subject = 'api接口测试邮件' # 邮件主题
sender = smtp_user # 邮件发送人
receiver = '1285823305@qq.com' # 邮件接收人

is_send_email = False # 是否发送邮件开关


if __name__=="__main__": # 测试本模块数据
    print(prj_path)
    print(data_path)
    print(test_case_path)
    print(report_path)
    print(log_path)