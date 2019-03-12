# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from pageElement.login_page_another import Login_page_another
from common.base import Base
import time

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver=webdriver.Chrome()
        # cls.login=Login_page(cls.driver)
        print("用例前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("用例后执行一次")
        # cls.driver.quit()

    def setUp(self):
        print("测试case前执行一次")
        self.driver = webdriver.Chrome()
        self.qqEmail = Login_page_another(self.driver)
        self.driver.get("https://mail.qq.com/cgi-bin/loginpage")
        self.driver.delete_all_cookies()  # 删除cookie，避免影响后续的登陆操作
        self.driver.refresh()  # 刷新界面
        time.sleep(2)

    def tearDown(self):
        print("测试case执行后执行一次")
        self.driver.close()
        self.driver.quit()

    def test_loginSuccess_01(self):
        """登陆成功case"""
        print("登陆成功")
        self.qqEmail.switchFram()
        self.qqEmail.input_username("848257135")
        self.qqEmail.input_password("########")
        self.qqEmail.click_login_button()
        time.sleep(2)
        login_title=self.qqEmail.is_login_success()
        print(login_title)
        self.assertEqual("QQ邮箱", login_title)

    def test_loginFail_02(self):
        """登陆失败case"""
        print("登陆失败")
        self.qqEmail.switchFram()
        self.qqEmail.input_username("848257135")
        self.qqEmail.input_password("@@@@@@@@@@@@@@@")
        self.qqEmail.click_login_button()
        time.sleep(2)
        login_title_fail = self.qqEmail.is_login_success()
        print(login_title_fail)
        self.assertNotEqual("QQ邮箱", login_title_fail)


if __name__ == '__main__':
    unittest.main()