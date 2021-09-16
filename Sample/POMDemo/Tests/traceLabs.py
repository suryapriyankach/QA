from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:/Selenium/Task/chromedriver_win32/chromedriver.exe")
driver.get("https://etherscan.io/register")
driver.maximize_window()
driver.find_element(By.ID, "ContentPlaceHolder1_txtUserName").click()
driver.find_element(By.ID, "ContentPlaceHolder1_txtUserName").send_keys("priya")
driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").click()
driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys("priya@gmail.com")
driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword").send_keys("Hello@123")
driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword2").send_keys("Hello@123")
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
"label[for='ContentPlaceHolder1_MyCheckBox']"))))
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
"label[for='ContentPlaceHolder1_SubscribeNewsletter']"))))
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark").click()



