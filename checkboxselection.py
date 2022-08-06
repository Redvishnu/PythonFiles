import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for check in checkboxes:
    if check.get_attribute("value")=="option2":
        check.click()
        assert check.is_selected()
        break
radio = radio = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radiobut in radio:
    if radiobut.get_attribute("value")=="radio1":
        radiobut.click()
        break

assert  driver.find_element(By.ID,'displayed-text').is_displayed()
driver.find_element(By.ID,'hide-textbox').click()
#assert  driver.find_element(By.ID,'displayed-text').is_displayed()

driver.find_element(By.ID,'name').send_keys("vishnu")
driver.find_element(By.ID,'alertbtn').click()
alert = driver.switch_to.alert
a = alert.text
print(a)
alert.accept()
driver.find_element(By.ID,'confirmbtn').click()
alert.dismiss()