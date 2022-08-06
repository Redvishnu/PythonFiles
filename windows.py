import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Click Here').click()
windowhandle =driver.window_handles
driver.switch_to.window(windowhandle[1])
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.switch_to.window(windowhandle[0])
print(driver.find_element(By.TAG_NAME,'h3').text)