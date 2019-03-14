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
    def __init__(self, driver:webdriver.Chrome):
        self.driver=driver
        self.timeout = 10
        self.poll_frequency = 0.5

    def findElement(self, locator):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象
        """
        #方法二次封装Demo
        #WebDriverWait(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
        #elen = WebDriverWait(driver, timeout, t).until(lambda x: x.findElenmentById("name"))元素显示等待
        #locator定位器，locator(by,value)即是传入元素定位器和元素值)
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：locator=(By.XX,"value")')
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            try:
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_element(*locator))
                return elem
            except:
                return print("定位不到元素")



    def findElements(self, locator):
        """

        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*locator))
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

    def switchToFrame(self, locator):
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

    def move_to_element(self,locator):
        """
        鼠标悬停事件操作
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem=self.findElement(locator)
        ActionChains(self.driver).move_to_element(elem).perform()

    def select_by_index(self,locator,index=0):
        """
        根据索引选中下拉框
        :param locator:
        :param index:
        :return:
        """
        elem=self.findElement(locator)
        Select(elem).select_by_index(index)

    def select_by_value(self,locator,value):
        """
        根据下拉选项的value值选中下拉框
        :param locator:
        :param value:
        :return:
        """
        elem=self.findElement(locator)
        Select(elem).select_by_value(value)

    def select_by_text(self,locator,text):
        """
        根据下拉选项的文本值选中下拉框
        :param locator:
        :param text:
        :return:
        """
        elem=self.findElement(locator)
        Select(elem).select_by_visible_text(text)

    def js_scroll_bottom(self):
        """
        滚动到屏幕底部
        :return:
        """
        js_height="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_height)

    def js_focus(self,locator):
        """
        聚焦元素,执行滚动事件到元素出现的位置
        :param locator:
        :return:
        """
        target=self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        """
        回到顶部
        :return:
        """
        js_top="window.scrollTo(0,0)"
        self.driver.execute_script(js_top)


if __name__=="__main__":

    baidu=Base(webdriver.Chrome())
    baidu.driver.get("https://www.baidu.com")
    locator=(By.LINK_TEXT,"设置")
    elen=baidu.findElement(locator)
    print(elen)
    ActionChains(baidu.driver).move_to_element(elen).perform()
    locator2=(By.LINK_TEXT,"搜索设置")
    baidu.click(locator2)
    baidu.driver.close()#大家在进行自动化测试的时候，一定要记得关闭浏览器，杀掉进程
    baidu.driver.quit()


