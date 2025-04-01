import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    browser.config.driver = driver

    yield
    driver.quit()