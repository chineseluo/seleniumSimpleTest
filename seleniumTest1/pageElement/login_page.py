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

class Login_page(Base):


    def login(self,username,password):
        locator_login_frame=(By.ID,"login_frame")
        self.switchToFrame(locator_login_frame)
        locator_username=(By.ID,"u")
        self.sendKey(locator_username,username)
        locator_password=(By.ID,"p")
        self.sendKey(locator_password,password)
        locator_login_button=(By.ID,"login_button")
        self.click(locator_login_button)

    def is_login_success(self):
        try:
            login_title = self.driver.title
            return login_title
        except:
            return " "

    def login_fail(self,username,password):
        time.sleep(2)
        self.login(username,password)
        time.sleep(2)
        login_title = self.is_login_success()
        print(login_title)
        return login_title

    def login_success(self,username,password):
        self.login(username,password)
        time.sleep(2)
        login_title = self.is_login_success()
        print(login_title)
        locator_mainFrame = (By.ID, "mainFrame")
        self.switchToFrame(locator_mainFrame)
        locator_today_alias = (By.ID, "today_alias")
        self.click(locator_today_alias)
        print(login_title)
        return login_title