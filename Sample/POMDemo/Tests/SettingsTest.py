import unittest
import time
import HtmlTestRunner


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Sample.POMDemo.Pages.LoginPage import LoginPage
from Sample.POMDemo.Pages.SettingPage import SettingPage


class SettingsTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()
        cls.stn = SettingPage(cls.driver)  # Global variables
        cls.login = LoginPage(cls.driver)



    def test_login_valid(self):

        self.driver.get("http://153.71.5.148/MyManagement")

        self.login.enter_username("admin")
        self.login.enter_password("admin")
        self.login.click_login()
        time.sleep(5)


    def test_setting_tile(self):

        self.stn.click_settingstile()
        time.sleep(5)
        self.stn.enter_username("Pri")
        self.stn.enter_password("priya1")
        self.stn.enter_confirmpassword("priya1")
        self.stn.click_save()
        time.sleep(6)
        self.stn.click_close()


    def test_user2(self):
        self.stn.enter_username("Priya2")
        self.stn.enter_password("priya1")
        self.stn.enter_confirmpassword("priya1")
        self.stn.click_save()
        time.sleep(6)
        self.stn.click_close()



    @classmethod
    def tearDownClass(cls):
        cls.driver.find_element(By.XPATH, "//a[@id='logoffbutton']").click()
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner)
