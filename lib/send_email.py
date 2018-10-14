# coding:utf-8

'''发送邮件'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
sys.path.append('..') # 提升一级项目搜索路径
import os
from config import config as cf

# 发送测试报告
def send_report():
    msg = MIMEMultipart() # 声明一个混合格式邮件对象

    # 邮件正文
    body = MIMEText('测试报告','plain','utf-8') # plain 表示普通文本，html 邮件格式为html
    msg.attach(body)

    # 邮件头
    msg['From'] = cf.sender
    msg['To'] = cf.receiver
    msg['Subject'] = cf.subject

    # 报告附件
    with open(cf.report_path,'rb') as f:
        att_file = f.read()
    att1 = MIMEText(att_file,'base64','utf-8') # base64用于非文本格式文件的传输
    att1["Content-Type"] = 'application/octet-stream' # 文件内容类型
    att1["Content-Disposition"] = 'attachment; filename="report.html"' # 文件内容描述
    msg.attach(att1)

    # 发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_user,cf.smtp_password)
    smtp.sendmail(cf.sender,cf.receiver,msg.as_string())
    cf.logging.info('邮件发送完成')

if __name__=='__main__':
    send_report()