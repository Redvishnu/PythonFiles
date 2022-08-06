import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PythonSelFramework.TestData.HomePageData import TesHomeData
from PythonSelFramework.pageObjects.HomePage import HomePage
from PythonSelFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self,Getdata):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(Getdata["firstname"])
        log.info("first" + Getdata["firstname"])
        homepage.getPassword().send_keys(Getdata["lastname"])
        homepage.getEmail().send_keys(Getdata["email"])
        log.info("entered all fields")



    #@pytest.fixture(params=[("vishnu","reddy",'dd@mail.com'),("ram",'sam','mm@gmail.com')])

    @pytest.fixture(params=TesHomeData.test_home_pageData)
    def Getdata(self,request):
        return request.param
        #self.selectOptionByText(homepage.getGender(), "Male")
        #driver.find_element(By.ID, 'username').clear()
        #driver.find_element(By.LINK_TEXT, 'Forgot Your Password?').click()
        #driver.find_element(By.XPATH, '//input[@name="cancel"]').click()
        # driver.find_element(By.XPATH,'//div[@id="usernamegroup"]/label').send_keys('vishnu')
        #print(driver.find_element(By.CSS_SELECTOR, 'form[name="login"] label:nth-child(3)').text)

