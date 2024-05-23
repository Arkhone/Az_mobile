from appium import webdriver


def initialize_appium_driver():
    desired_caps = {
        'platformName': 'Android',  # или 'iOS'
        'platformVersion': 'ваша_версия_платформы',
        'deviceName': 'Android',
        'app': 'app/lg-st-2305-1.apk',
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
