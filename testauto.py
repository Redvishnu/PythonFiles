from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,'name').send_keys("vishnu")
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.ID, 'exampleCheck1').click()
driver.find_element(By.XPATH,'//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]').click()
a = driver.find_element(By.XPATH,'/html/body/app-root/form-comp/div/div[2]/div').text
print(a)
 