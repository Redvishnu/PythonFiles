import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
time.sleep(2)
veg = driver.find_elements(By.XPATH,'//div[@class="products"]/div')
count = len(veg)
assert count>0
for result in veg:
    result.find_element(By.XPATH,'div/button').click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("vishnu")
driver.find_element(By.XPATH," //button[text()='Apply']").click()
wait =  WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)

amount = driver.find_elements(By.XPATH,'//tr/td[5]/p')
totalamt = int(driver.find_element(By.CSS_SELECTOR,'.totAmt').text)
sum = 0
for amounts in amount:
    if amounts.text == totalamt:
        assert print(sum)
    else:
        sum = sum + int(amounts.text)
print(sum)



