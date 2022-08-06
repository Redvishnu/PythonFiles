import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID,'autosuggest').send_keys("Ind")
driver.find_element(By.XPATH,"").send_keys("vishnu")
time.sleep(2)
lis = driver.find_elements(By.CSS_SELECTOR,'li[class="ui-menu-item"] a')
for i in lis:
    if i.text == "India":
       i.click()
       break


count = len(veg)
assert count>0
for result in veg:
    result.find_element(By.XPATH,'div/button').click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("vishnu")
driver.find_element(By.XPATH," //button[text()='Apply']").click()