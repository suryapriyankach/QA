from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:/Selenium/Task/chromedriver_win32/chromedriver.exe")
driver.get("https://www.autohero.com/de/search/")
driver.maximize_window()
driver.find_element(By.XPATH, '//button[@id="carMakeFilter"]').click()
driver.find_element(By.XPATH, '//li[@Class="listItem___3FT95"]//input[@value="Volkswagen"]').click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//li[@Class="listItem___1KT4l"][5]//input[@Value="Golf"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//button[@id="mileageFilter"]').click()
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '//select[@id="rangeEnd"][contains(@data-qa-selector,"select-mileage-to")]')
element.click()
drp = Select(element)
drp.select_by_index("2")
driver.find_element(By.XPATH, '//div').click()

lst = driver.find_elements(By.TAG_NAME, 'h2')
driver.implicitly_wait(30)
print(len(lst))
for i in lst:
    print(i.text)
    time.sleep(5)
driver.close()

for test in list1:
    if 'Volks' and 'Golf' in str(list1):
        assert True
    else:
        assert False

    if '25.000 km' <= str(list3):
        assert True
    else:
        assert False