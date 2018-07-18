# -*- coding:utf-8 -*-
#date:  2018/7/15
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#------LOG配置------
LOG_LEVER = 'debug'

LOG_NAME = 'UI_TEST.log'



#------邮件配置------
MAIL_HOST = 'smtp.qq.com'
USER = '2890104046@qq.com'
PASSWORD = 'xybzqknuhdgfddah'
TO = [
    '136945832@qq.com',
    '875580931@qq.com'
]

BASE_URL = 'https://www.dingdanggj.com/pms'








#-------数据库配置-------
MYSQL_INFO = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'passwd':'Shen19920616',
    'charset':'utf8',
    'db':'shenyong_test'
}