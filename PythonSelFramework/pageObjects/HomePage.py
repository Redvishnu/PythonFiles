from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    name = (By.NAME,'name')
    email = (By.NAME,'email')
    password = (By.ID,'exampleInputPassword1')
    #gender = Select((By.ID, "exampleFormControlSelect1"))

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    #def getGender(self):
        #return self.driver.find_element(*HomePage.gender)