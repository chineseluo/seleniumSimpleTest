# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from common.base import Base
import time

class Login_page_another(Base):
    locator_login_frame = (By.ID, "login_frame")
    locator_username = (By.ID, "u")
    locator_password = (By.ID, "p")
    locator_login_button = (By.ID, "login_button")

    def switchFram(self):
        self.switchToFrame(self.locator_login_frame)

    def input_username(self,text=""):
        """输入用户名"""
        self.sendKey(self.locator_username,text)

    def input_password(self,text=""):
        """输入密码"""
        self.sendKey(self.locator_password,text)

    def click_login_button(self):
        """点击登陆"""
        self.click(self.locator_login_button)

    def is_alert_exist(self):
        """
        判断是否有弹出框
        :return:
        """
        try:
            time.sleep(2)
            alert=self.driver.switch_to.alert
            text=alert.text
            alert.accept()
            return text
        except:
            return ""

    def is_login_success(self):
        try:
            login_title = self.driver.title
            return login_title
        except:
            return " "