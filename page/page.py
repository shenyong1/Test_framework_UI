# -*- coding:utf-8 -*-
#date:  2018/7/15
from lib.pyse import Pyse

#基础页面类，处理浏览器等基础的页面操作
class BasePage(object):
    #初始化一个浏览器对象
    def __init__(self):
        self.pyse = Pyse('chrome')

    #发送一个Http请求
    def open(self,url):
        self.pyse.open(url)

    #关闭当前页面
    def close(self):
        self.pyse.close()

    #关闭程序
    def quit(self):
        self.pyse.quit()

class LoginPage(BasePage):
    def send_username(self):
        css = 'css=>[placeholder="手机号"]'
        self.pyse.type(css,'18221293942')

    def send_passwd(self):
        css = 'css=>[placeholder="密码"]'
        self.pyse.type(css,'123456')

    def login_click(self):
        css = 'css=>[data-cid="登录"]'
        self.pyse.click(css)

    def check_login(self,name):
        css = 'css=>.user-name'
        res = self.pyse.wait_and_save_exception(css,name)
        return res