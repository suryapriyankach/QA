from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:/Selenium/Task/chromedriver_win32/chromedriver.exe")
driver.get("https://www.autohero.com/de/search/?brand=VOLKSWAGEN&model=VOLKSWAGEN.Golf&mileageMax=25000")
driver.maximize_window()

#lst = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]//div//a//div//div//h2[@class="title___uRijL adTitle___1MVoL"][contains(@data-qa-selector,"title")])]')
lst = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]//div//a//div//div//h2[@class="title___uRijL adTitle___1MVoL"][contains(@data-qa-selector,"title"]')
driver.implicitly_wait(30)
list1 = ([elm.text for elm in lst])
print(len(list1))
print(list1)
