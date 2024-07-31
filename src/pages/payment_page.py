from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

from src.utils.config import USERNAME, PASSWORD


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.payments_button = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-sidebar[1]/div[1]/aside[1]/div[2]/div[1]/a[2]/span[2]")
        self.send_button = (By.ID, "poiActive")
        self.popup_button = (By.XPATH, "/html[1]/body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]")
        self.beneficiary_input = (By.ID, "beneficiaryInput")
        self.beneficiary_option = (By.XPATH,
                                   "/html[1]/body[1]/div[5]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-single-payment-send[1]/div[1]/mat-dialog-content[1]/mat-stepper[1]/div[1]/div[2]/div[1]/app-single-payment-send-step1[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/span[1]")
        self.select_beneficiary_button = (By.XPATH, "/html[1]/body[1]/div[5]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-single-payment-send[1]/div[1]/mat-dialog-content[1]/mat-stepper[1]/div[1]/div[2]/div[1]/app-single-payment-send-step1[1]/div[1]/div[3]/div[1]/div[1]/button[1]")

        self.amount_input = (By.ID, "amount_forpayment_single_payment")
        self.next_button = (By.XPATH,
                            "/html[1]/body[1]/div[5]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-single-payment-send[1]/div[1]/mat-dialog-content[1]/mat-stepper[1]/div[1]/div[2]/div[1]/app-single-payment-send-step1[1]/div[1]/div[3]/button[2]")

        self.payment_notes = (By.XPATH,
                              "/html[1]/body[1]/div[5]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-single-payment-send[1]/div[1]/mat-dialog-content[1]/mat-stepper[1]/div[1]/div[2]/div[2]/app-single-payment-send-step2[1]/div[1]/div[3]/div[1]/form[1]/div[1]/textarea[1]")
        self.next_button_step2 = (By.ID, "goToNext_single_payment2")

        self.cost_option = (By.ID, "cost1_btn_single_payment3-input")
        self.approve_checkbox = (By.ID, "approve_checkbox_single_payment3-input")
        self.final_next_button = (By.XPATH,
                                  "/html[1]/body[1]/div[5]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-single-payment-send[1]/div[1]/mat-dialog-content[1]/mat-stepper[1]/div[1]/div[2]/div[3]/app-single-payment-send-step3[1]/div[1]/div[3]/button[1]")

        self.success_message = (By.XPATH,
                                "/html[1]/body[1]/div[5]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-single-payment-send[1]/div[1]/mat-dialog-content[1]/mat-stepper[1]/div[1]/div[2]/div[4]/app-single-payment-send-completed[1]/div[1]/div[3]/div[1]/h2[1]/strong[1]")

    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} did not appear within {timeout} seconds")
            raise


    def navigate_to_payments(self):
        self.wait_for_element(self.payments_button).click()

    def click_send_button(self):
        self.wait_for_element(self.send_button).click()

    def handle_popup(self):
        self.wait_for_element(self.popup_button).click()

    def select_beneficiary(self):
        self.wait_for_element(self.beneficiary_input).click()
        self.wait_for_element(self.beneficiary_option).click()
        self.wait_for_element(self.select_beneficiary_button).click()

    def enter_payment_amount(self, amount):
        amount_element = self.wait_for_element(self.amount_input)
        amount_element.clear()
        amount_element.send_keys(amount)

    def click_next_button(self):
        self.wait_for_element(self.next_button).click()

    def enter_payment_notes(self, notes):
        notes_element = self.wait_for_element(self.payment_notes)
        notes_element.clear()
        notes_element.send_keys(notes)

    def click_next_button_step2(self):
        self.wait_for_element(self.next_button_step2).click()

    def select_cost_option(self):
        self.wait_for_element(self.cost_option).click()

    def approve_terms(self):
        self.wait_for_element(self.approve_checkbox).click()

    def click_final_next_button(self):
        self.wait_for_element(self.final_next_button).click()

    def verify_payment_success(self):
        success_element = self.wait_for_element(self.success_message)
        assert success_element.is_displayed(), "Success message is not displayed"
        assert success_element.text == "Sent Successfully", f"Expected 'Sent Successfully', but got '{success_element.text}'"

    def initiate_payment_process(self):
        self.navigate_to_payments()
        time.sleep(2)
        self.click_send_button()
        time.sleep(2)
        self.handle_popup()
        time.sleep(2)
        self.select_beneficiary()
        time.sleep(2)
        self.enter_payment_amount("120")
        time.sleep(2)
        self.click_next_button()
        time.sleep(2)
        self.click_next_button()
        time.sleep(2)
        self.enter_payment_notes("testing notes")
        time.sleep(2)
        self.click_next_button_step2()
        time.sleep(2)
        self.select_cost_option()
        time.sleep(2)
        self.approve_terms()
        time.sleep(2)
        self.click_final_next_button()
        time.sleep(2)
        self.verify_payment_success()