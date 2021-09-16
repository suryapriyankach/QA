from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


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
driver.find_element(By.XPATH, '//button[@id="mileageFilter"]').click()
#driver.find_element(By.XPATH, '//div').click()

brand = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]//div//div//div//h2')
driver.implicitly_wait(30)
list1 = ([elm.text for elm in brand])

klm = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]//div//div//ul/li[3]')
driver.implicitly_wait(20)
list2 = ([elms.text for elms in klm])

list3 = []
for string in list2:
    new_string = string.replace("•\n", "")
    list3.append(new_string)

filterData = list1 + list3
if ('Volks' and 'Golf' in str(filterData)) and ('25.000 km' <= str(filterData)):
    assert True
    print("Assertion Passed")
else:
    assert False

driver.close()


















