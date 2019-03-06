# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

class Base:
    def __init__(self,driver):
        self.driver=driver
        self.timeout = 10
        self.poll_frequency = 0.5

    def findElement(self,locator):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象
        """
        #方法二次封装Demo
        #WebDriverWait(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
        #elen = WebDriverWait(driver, timeout, t).until(lambda x: x.findElenmentById("name"))元素显示等待
        #locator定位器，locator(by,value)即是传入元素定位器和元素值
        elem=WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(lambda x:x.find_element(*locator))
        return elem

    def findElements(self, locator):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        elem = WebDriverWait(driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*locator))
        return elem

    def sendKey(self,locator,value):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :param value: 传入输入的值
        :return:
        """
        elem=self.findElement(locator)
        elem.send_keys(value)

    def click(self,locator):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem=self.findElement(locator)
        elem.click()

    def switchToFrame(self,locator):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem = self.findElement(locator)
        self.driver.switch_to.frame(elem)

    def elementIsBeSelected(self,locator):
        """
        判断元素是否被选中，用于单选或者复选框
        :param locator:  传入定位器参数locator=(By.XX,"value")
        :return: 返回布尔值True，False
        """
        elem=self.findElement(locator)
        result=elem.is_selecter()
        return result

    def isElementExist(self,locator):
        """
        判断元素是否存在
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回布尔值True，False
        """
        try:
            elem=self.findElement(locator)
            return True
        except:
            return False

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    baidu=Base(driver)
    locator=(By.LINK_TEXT,"设置")
    elen=baidu.findElement(locator)
    ActionChains(driver).move_to_element(elen).perform()
    locator2=(By.LINK_TEXT,"搜索设置")
    baidu.click(locator2)
    driver.close()#大家在进行自动化测试的时候，一定要记得关闭浏览器，杀掉进程
    driver.quit()


