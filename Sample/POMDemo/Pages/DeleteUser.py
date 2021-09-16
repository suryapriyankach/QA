from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

class DeleteUser():

    def __init__(self, driver):
        self.driver = driver

        self.driver.click_dropdown_id = "UserDropDownList"
        self.driver.click_delete_button_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[2]/div[3]/input[1]"
        self.driver.click_ok_button_id = "popupConfirmOk"
        self.driver.popup_button_xpath = "//a[@id='popupMessageCloseButton']"

    def click_dropdown(self,name):
        self.driver.find_element(By.ID, self.driver.click_dropdown_id).click()
        Select.select_by_visible_text(name).click()



    def click_delete_button(self):
        self.driver.find_element(By.XPATH, self.driver.click_delete_button_xpath).click()

    def click_ok_button(self):
        self.driver.find_element(By.XPATH, self.driver.click_ok_button_id).click()









