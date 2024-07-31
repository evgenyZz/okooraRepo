Automation scripting  - Given access to okoora's demo env , please write an autimated test script for pament scenario


Due to time limitation unfortunately I wasn't able to finish the whole testing process and did only a basic flow that will assert only the final result
the "Sent successfully " in the end of the process.

More time given I would implement all the tests that I provided in the Okoora Qa Team Lead assignment document.

every test would have an assert for the wanted result and the flow would be broken into smaller pieces to test each element and action in
the web page.

the sleep(2) in def initiate_payment_process(self) function is purely for debugging and are not needed
the approach for wait for element should be used here - to wait until the element is visible and interactive -

The user/pass file shouldn't of course be included in the project but for convenience I left it here.

this is a quick summery of what you can find here in the project :

what is the project ?
Payment Platform Automation Testing
Project Overview
This project implements automated testing for a payment platform using Selenium WebDriver with Python. It focuses on testing the end-to-end payment process, from user login to successful payment confirmation.

Key Features

Automated login process
Navigation through the payment workflow
Beneficiary selection
Payment amount entry
Addition of payment notes
Selection of payment options
Final payment confirmation
Verification of successful payment

Technology Stack

Python 3.9
Selenium WebDriver
pytest
Page Object Model (POM) design pattern

Test Scenario
The main test scenario covers a happy path through the payment process:

User login
Navigate to the payments section
Initiate a new payment
Select a beneficiary
Enter payment amount
Add payment notes
Select payment options
Confirm payment
Verify successful payment message

Project Structure

src/: Contains the main source code

pages/: Page object classes for different pages in the application
utils/: Utility functions and configuration


tests/: Contains the test scripts
conftest.py: pytest configurations and fixtures

Running the Tests
you can run the  test_payment_flow.py file

This project demonstrates the use of Selenium WebDriver for automating web application testing, specifically for a complex workflow like an online payment system. It showcases best practices in test automation, including the use of the Page Object Model for maintainability and readability.