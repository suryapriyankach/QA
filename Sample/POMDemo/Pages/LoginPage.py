from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.driver_Username_textbox_id = "UserName"
        self.driver_Password_textbox_id = "Password"
        self.driver_Login_button_xpath = "/html/body/div[1]/div[2]/div/form/div/ul/li[4]/table/tbody/tr/td/div/input"
        self.driver_Logout_button_xpath = "//a[@id='logoffbutton']"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.driver_Username_textbox_id).clear()
        self.driver.find_element(By.ID, self.driver_Username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.driver_Password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.driver_Login_button_xpath).click()


    def click_logout(self):
        self.driver.find_element(By.XPATH, self.driver_Logout_button_xpath).click()
