import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
#action.double_click(By.XPATH,'')
#action.context_click()
#action.drag_and_drop()
time.sleep(2)
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
#action.context_click((driver.find_element(By.LINK_TEXT,'Top'))).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,'Reload')).click().perform()