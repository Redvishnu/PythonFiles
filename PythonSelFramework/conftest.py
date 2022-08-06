import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "firefox":
        print("null")
    request.cls.driver = driver
    yield
    driver.quit()
    #driver.close()