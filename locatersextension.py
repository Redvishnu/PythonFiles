from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.maximize_window()
driver.find_element(By.ID,'username').send_keys('vishnu')
driver.find_element(By.ID,'username').clear()
driver.find_element(By.LINK_TEXT,'Forgot Your Password?').click()
driver.find_element(By.XPATH,'//input[@name="cancel"]').click()
#driver.find_element(By.XPATH,'//div[@id="usernamegroup"]/label').send_keys('vishnu')
print(driver.find_element(By.CSS_SELECTOR,'form[name="login"] label:nth-child(3)').text)

