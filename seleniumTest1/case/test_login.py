# coding:utf-8
import unittest
from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from pageElement.login_page import Login_page
import time


class login_EmailTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver=webdriver.Chrome()
        # cls.login=Login_page(cls.driver)
        print("用例前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("用例后执行一次")
        #cls.driver.quit()

    def setUp(self):
        print("用例执行前执行一次")
        self.driver = webdriver.Chrome()
        self.qqEmail=Login_page(self.driver)
        self.driver.get("https://mail.qq.com/cgi-bin/loginpage")
        self.driver.delete_all_cookies()#删除cookie，避免影响后续的登陆操作
        self.driver.refresh()#刷新界面
        time.sleep(2)

    def tearDown(self):
        print("用例执行后执行一次")
        self.driver.close()
        self.driver.quit()

    def test_loginSuccess(self):
        """登陆成功case"""
        login_title=self.qqEmail.login_success("848257135", "##########")
        self.assertEqual("QQ邮箱",login_title)

    def test_loginFail(self):
        """登陆失败case"""
        login_title=self.qqEmail.login_fail("848257135", "@@@@@@@@@@@")
        self.assertNotEqual("QQ邮箱",login_title)

if __name__ == '__main__':
    unittest.main()