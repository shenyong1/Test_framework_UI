# -*- coding:utf-8 -*-
#date:  2018/6/3
import logging,os
from logging import handlers
from conf.setting import LOG_NAME
from conf.path import LOG_PATH


class Logger(object):
    def __init__(self,file_name,level='info',when = 'D'):
        self.logger = logging.getLogger()
        self.logger.setLevel(self.log_level(level))
        log_file_name = os.path.join(LOG_PATH,file_name)
        #文本对象
        self.filelogger = handlers.TimedRotatingFileHandler(filename=log_file_name,
                                                            backupCount=10,
                                                            encoding='utf8',
                                                            when=when
                                                            )
        #控制台输出对象
        self.consolelogger = logging.StreamHandler()
        self.consolelogger.setLevel(self.log_level(level))

        #日志格式
        self.formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
        )

        self.filelogger.setFormatter(self.formater)
        self.consolelogger.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.consolelogger)



    def log_level(self,lev):
        level = {
            'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'critical':logging.CRITICAL
        }
        lev = lev.lower()
        return level.get(lev)

logger = Logger(LOG_NAME).logger

if __name__ == '__main__':
    test = Logger(LOG_NAME).logger
    test.info('78945612')
