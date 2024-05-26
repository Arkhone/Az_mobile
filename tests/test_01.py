import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep


@pytest.fixture(scope="module")
def appium_driver():
    aps = {
        "platformName": "Android",
        "deviceName": "Android_11",
        "app": "/app/lg-st-2305-1.apk",
        "automationName": "UiAutomator2"
    }
    ds = UiAutomator2Options().load_capabilities(aps)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=ds)
    yield driver
    driver.quit()


def test_open_app(appium_driver):
    sleep(5)  # Wait for the app to open
    assert appium_driver.current_activity is not None
