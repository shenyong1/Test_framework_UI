import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 报告地址
REPOR_TPATH = os.path.join(BASE_PATH,'report')

LOG_PATH = os.path.join(BASE_PATH,'log')


#用例存放地址
WEBCASE_PATH = os.path.join(BASE_PATH,'test_case')

#报告截图存放地址
WEBPICTURE_PATH = os.path.join(REPOR_TPATH,'picture/')


