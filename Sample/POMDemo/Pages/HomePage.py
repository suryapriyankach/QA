from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.driver.about_button_xpath = "//input[@id='aboutButton']"
        self.driver.close_button_xpath = "//a[@id='popupMessageCloseButton']"
        self.driver.logoff_button_xpath = "//a[@id='logoffbutton']"

    def click_about(self):
        self.driver.find_element(By.XPATH, self.driver.about_button_xpath).click()

    def click_close(self):
        self.driver.find_element(By.XPATH, self.driver.close_button_xpath).click()


    def click_logoff_button(self):
        self.driver.find_element(By.XPATH, self.driver.logoff_button_xpath).click()



