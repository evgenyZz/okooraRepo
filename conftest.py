import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.pages.login_page import LoginPage
from src.pages.payment_page import PaymentPage
from src.utils.config import BASE_URL

CHROMEDRIVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver'))


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    driver.get(BASE_URL)
    return LoginPage(driver)


@pytest.fixture(scope="function")
def payment_page(driver):
    return PaymentPage(driver)