# -*- coding:utf-8 -*-
#date:  2018/5/28
import unittest
from page.page import LoginPage
from conf.setting import BASE_URL

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = LoginPage()
        cls.page.open(BASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_login(self):
        self.page.send_username()
        self.page.send_passwd()
        self.page.login_click()
        self.assertTrue(self.page.check_login('test_login'))


if __name__ == '__main__':
    unittest.main()
