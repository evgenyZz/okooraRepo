from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "email_field")
        self.password_input = (By.ID, "password_field")
        self.login_button = (By.ID, "button_login")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()