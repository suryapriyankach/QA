from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://153.71.5.148/MyManagement/")
driver.maximize_window()

driver.find_element(By.ID, 'UserName').send_keys("admin")
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/input[1]").click()
driver.implicitly_wait(10)
print("saved")
driver.save_screenshot(r"C:\Users\sc185281\Desktop\Germany\ss.png")




driver.close()