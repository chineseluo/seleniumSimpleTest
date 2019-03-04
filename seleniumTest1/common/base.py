import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class Base:
    def __init__(self,driver):
        self.driver=driver
        self.timeout = 10
        self.poll_frequency = 0.5

    def FindElement(self,locator):
        #方法二次封装Demo
        #WebDriverWait(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
        #elen = WebDriverWait(driver, timeout, t).until(lambda x: x.findElenmentById("name"))元素显示等待
        #locator定位器，locator(by,value)即是传入元素定位器和元素值
        elen=WebDriverWait(driver,self.timeout,self.poll_frequency).until(lambda x:x.find_element(*locator))
        return elen

    def FindElements(self, locator):
        eles = WebDriverWait(driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*locator))
        return eles

if __name__=="__main__":
    driver=webdriver.Chrome(executable_path="C:/python/chromedriver.exe")
    driver.get("https://mail.qq.com/cgi-bin/loginpage")
    driver.switch_to.frame(driver.find_element_by_id("login_frame"))
    qqEmail=Base(driver)
    locator=(By.ID, "u")
    qqEmail.FindElement(locator).send_keys("848257135")
    driver.close()#大家在进行自动化测试的时候，一定要记得关闭浏览器，杀掉进程
    driver.quit()


