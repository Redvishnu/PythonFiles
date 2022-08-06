import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,'a[href="/angularpractice/shop"]').click()
products = driver.find_elements(By.XPATH,'//h4[@class="card-title"]')
for product in products:
    if product == 'Blackberry':
        s = product.text
        print(s)
        product.find_element(By.XPATH,'//button[@class="btn btn-info"]').click()

