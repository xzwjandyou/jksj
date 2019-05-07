# !/usr/bin/python
# -*- coding:utf-8 -*-

import  sys
# reload(sys)
# sys.setdefaultencoding('UTF8')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import copy

chrome_options = webdriver.ChromeOptions()

username = ''
password = ''
loginUrl = 'https://account.geekbang.org/login?redirect=https%3A%2F%2Ftime.geekbang.org%2F'

class Jksj(object):
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_size(1800, 1000)
    browser.set_page_load_timeout(30)
    browser.implicitly_wait(5)
    wait = WebDriverWait(browser, 10)
    current_url = ''

    def login(self, url):

        self.browser.get(url)
        self.browser.find_element_by_class_name("nw-input").clear()
        self.browser.find_element_by_class_name("nw-input").send_keys(username)
        self.browser.find_element_by_xpath('//div[@class="input-wrap"]//input[@class="input"]').send_keys(password)
        self.browser.find_element_by_class_name("mybtn").click()


    def checkIfLogout(self):
        while (1):
            try:
                self.switch_window()
                logoutMask = self.browser.find_element_by_class_name('confirm-box-wrapper')
                print(logoutMask)
                if (logoutMask):
                    time.sleep(2)
                    self.login(loginUrl)
                    time.sleep(1)
                    self.browser.get(self.current_url)
            except:
                pass
                time.sleep(2)

    def switch_window(self):
        now = self.browser.current_window_handle
        all_handles = self.browser.window_handles
        if now != all_handles[-1]:
            self.browser.switch_to.window(all_handles[-1])
        self.current_url = copy.deepcopy(self.browser.current_url)


    def begin(self):
        #第一次登陆
        self.login(loginUrl)
        #切换主视角位当前窗口
        self.switch_window()
        self.checkIfLogout()

if __name__ == "__main__":
    jksj = Jksj()
    jksj.begin()