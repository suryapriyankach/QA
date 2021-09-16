from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class SettingPage():

    def __init__(self, driver):
        self.driver = driver

        self.driver.settings_tile_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[3]/div[3]"
        self.driver.usermanagement_tile_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[3]/div[1]"
        self.driver.users_tile_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[3]/div[1]"
        self.driver.new_user_dropdown_id = "UserDropDownList"
        self.driver.username_textbox_id = "//input[@id='UserNameBox']"
        self.driver.password_textbox_xpath = "//input[@id='PasswordBox']"
        self.driver.confirm_password_textbox_id = "ConfirmBox"
        self.driver.save_button_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[2]/div[1]/input[1]"
        self.driver.popup_button_linktext = "//a[@id='popupMessageCloseButton']"


    def click_settingstile(self):
        self.driver.find_element(By.XPATH, self.driver.settings_tile_xpath).click()
        self.driver.find_element(By.XPATH, self.driver.usermanagement_tile_xpath).click()
        self.driver.find_element(By.XPATH, self.driver.users_tile_xpath).click()

    def select_newuser(self):
        self.driver.find_element(By.ID, self.driver.new_user_dropdown_id).select_by_visibletext("New user")

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.driver.username_textbox_id).clear()
        self.driver.find_element(By.XPATH, self.driver.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.driver.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.driver.password_textbox_xpath).send_keys(password)

    def enter_confirmpassword(self, confirmpassword):
        self.driver.find_element(By.ID, self.driver.confirm_password_textbox_id).clear()
        self.driver.find_element(By.ID, self.driver.confirm_password_textbox_id).send_keys(confirmpassword)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.driver.save_button_xpath).click()

    def click_close(self):
        self.driver.find_element(By.XPATH, self.driver.popup_button_linktext).click()

