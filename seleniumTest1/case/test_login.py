import unittest
from selenium import webdriver
import time


class login_EmailTest(unittest.TestCase):
    def loginQQEmail(username, password):
        driver = webdriver.Chrome()
        driver.get("https://mail.qq.com/cgi-bin/loginpage")
        driver.switch_to.frame(driver.find_element_by_id("login_frame"))
        driver.find_element_by_id("u").send_keys(username)
        driver.find_element_by_id("p").send_keys(password)
        driver.find_element_by_id("login_button").click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()