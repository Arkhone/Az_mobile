import pytest
from appium import webdriver
from time import sleep


@pytest.fixture(scope="function")
def appium_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "app": "/app/lg-st-2305-1.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()
