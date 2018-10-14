# coding:utf-8

'''数据库操作'''

import pymysql
import sys
sys.path.append('..') # 提升包搜索路径到项目下
from config import config as cf

# 获取数据库连接
def get_conn():
    conn = pymysql.connect(host=cf.db_host,
                           port=cf.db_port,
                           user=cf.db_user,
                           password=cf.db_password,
                           db=cf.db,
                           charset='utf8')
    return conn

# 数据库查询
def db_query(sql):
    conn = get_conn() # 返回数据库连接
    cur = conn.cursor() # 建立游标
    cur.execute(sql) # 执行sql查询
    result = cur.fetchall() # 获取查询结果
    cf.logging.debug(sql) # 日志输出sql语句
    cf.logging.debug(result) # 日志输出查询结果
    return result

# 数据库修改
def db_check(sql):
    conn = get_conn()
    cur =conn.cursor()
    try:
        cur.execute(sql)
        cf.logging.debug(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e)) # 日志输出错误信息
    finally:
        cur.close()
        conn.close()

if __name__=='__main__':
    result = db_query("select * from user where name='张三'")
    print(result)
