import unittest
from selenium import webdriver
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
        self.driver.switch_to.frame(self.driver.find_element_by_id("login_frame"))
        self.driver.find_element_by_id("u").send_keys(username)
        self.driver.find_element_by_id("p").send_keys(password)
        self.driver.find_element_by_id("login_button").click()

    def test_loginSuccess(self):
        """登陆成功case"""
        self.login("848257135","#########")
        time.sleep(2)
        login_title=self.is_login_success()
        self.driver.switch_to.frame(self.driver.find_element_by_id("mainFrame"))
        self.driver.find_element_by_id("today_alias").click()
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