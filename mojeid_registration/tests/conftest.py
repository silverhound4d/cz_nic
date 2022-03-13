import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()