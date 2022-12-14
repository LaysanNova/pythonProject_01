

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
import os


@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox']

    browser = os.environ.get('BROWSER', 'chrome')

    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()

    if browser not in supported_browsers:
        raise Exception(f"Provided browser {browser} is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser in 'firefox':
        driver = webdriver.Firefox()
    elif browser in 'edge':
        driver = webdriver.Edge()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = driver

    yield
    driver.quit()