import pytest
import time
from src.utils.config import USERNAME, PASSWORD


def test_successful_payment_process(login_page, payment_page):
    login_page.login(USERNAME, PASSWORD)

    try:
        payment_page.initiate_payment_process()
        time.sleep(5)
    except AssertionError as e:
        pytest.fail(f"Payment process failed: {str(e)}")


