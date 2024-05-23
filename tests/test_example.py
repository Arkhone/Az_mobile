# tests/test_example.py
from utils.appium_utils import initialize_appium_driver
import pytest


@pytest.fixture(scope="function")
def appium_driver(request):
    driver = initialize_appium_driver()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


def test_example(appium_driver):
    # Ваш код теста с использованием appium_driver
    # Например:
    element = appium_driver.find_element_by_id("com.example.app:id/button")
    element.click()
    assert "Success" in appium_driver.page_source
