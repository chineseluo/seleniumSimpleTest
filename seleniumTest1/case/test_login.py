# coding:utf-8
import unittest
from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time


class login_EmailTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("用例前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("用例后执行一次")
        #cls.driver.quit()

    def setUp(self):
        print("用例执行前执行一次")
        self.driver = webdriver.Chrome()
        self.qqEmail=Base(self.driver)
        self.driver.get("https://mail.qq.com/cgi-bin/loginpage")
        time.sleep(2)

    def tearDown(self):
        print("用例执行后执行一次")
        self.driver.close()
        self.driver.quit()


    def is_login_success(self):
        try:
            login_title = self.driver.title
            return login_title
        except:
            return " "

    def login(self,username,password):
        locator_login_frame=(By.ID,"login_frame")
        self.qqEmail.switchToFrame(locator_login_frame)
        locator_username=(By.ID,"u")
        self.qqEmail.sendKey(locator_username,username)
        locator_password=(By.ID,"p")
        self.qqEmail.sendKey(locator_password,password)
        locator_login_button=(By.ID,"login_button")
        self.qqEmail.click(locator_login_button)

    def test_loginSuccess(self):
        """登陆成功case"""
        self.login("848257135","###########")
        time.sleep(2)
        login_title=self.is_login_success()
        print(login_title)
        locator_mainFrame=(By.ID,"mainFrame")
        self.qqEmail.switchToFrame(locator_mainFrame)
        locator_today_alias=(By.ID,"today_alias")
        self.qqEmail.click(locator_today_alias)
        print(login_title)
        self.assertEqual("QQ邮箱",login_title)

    def test_loginFail(self):
        """登陆失败case"""
        self.login("848257135","@@@@@@@@@@@")
        time.sleep(2)
        login_title = self.is_login_success()
        print(login_title)
        self.assertNotEqual("QQ邮箱",login_title)

if __name__ == '__main__':
    unittest.main()