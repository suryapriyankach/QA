from selenium import webdriver
import unittest
import time

from Sample.POMDemo.Pages.LoginPage import LoginPage
from Sample.POMDemo.Pages.HomePage import HomePage


class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)

    def test_login(self):
        driver = self.driver

        driver.get("http://153.71.5.148/MyManagement")
        self.login.enter_username("admin")
        self.login.enter_password("admin")
        self.login.click_login()
        time.sleep(8)

    def test_home_about(self):
        self.home.click_about()
        time.sleep(8)
        self.home.click_close()

    def logoff_click(self):
        self.logof.click_logoff_button()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
