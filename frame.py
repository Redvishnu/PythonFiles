import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,'tinymce').clear()
driver.find_element(By.ID,'tinymce').send_keys("my text entered in frame")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,'h3').text)