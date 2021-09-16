from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Sample.POMDemo.Pages.LoginPage import LoginPage
from Sample.POMDemo.Pages.DeleteUser import DeleteUser
from Sample.POMDemo.Pages.SettingPage import SettingPage

class Deleteuser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()
        cls.login = LoginPage(cls.driver) #class level variables
        cls.stn = SettingPage(cls.driver)
        cls.dl = DeleteUser(cls.driver)

    def test_login(self):
        self.driver.get("http://153.71.5.148/MyManagement")
        self.login.enter_username("admin")
        self.login.enter_password("admin")
        self.login.click_login()
        time.sleep(5)

    def test_navigate_users(self):
        self.stn.click_settingstile()
        time.sleep(5)
        self.dl.click_dropdown("Priya123")
        self.dl.click_delete_button()
        time.sleep(10)
        self.dl.click_ok_button()
        time.sleep(6)
        self.login.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()





