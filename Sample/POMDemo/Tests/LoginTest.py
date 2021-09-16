import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from Sample.POMDemo.Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()
        cls.login = LoginPage(cls.driver)

    def test_login_valid(self):
        driver = self.driver

        driver.get("http://153.71.5.148/MyManagement")
        self.login.enter_username("admin")
        self.login.enter_password("admin")
        self.login.click_login()
        time.sleep(8)

        wait = WebDriverWait(driver, 10)
        wait.until( EC.presence_of_element_located((By.XPATH, "//h4[@id='headerInfo']")))


        title = self.driver.title
        print('Title is: ' + title)

    def test_logout(self):
        self.login.click_logout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



if __name__ == '__main__':
    unittest.main()
