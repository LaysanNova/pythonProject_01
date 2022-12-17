from blaze.src.pages.locators.MyAccountLocator import MyAccountLocator
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.alert import Alert


class MyAccount(MyAccountLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self, username, password):
        self.sl.wait_and_click(MyAccount.LOGIN_IN)
        self.sl.wait_and_input_text(MyAccount.LOGIN_USER_NAME, username)
        self.sl.wait_and_input_text(MyAccount.LOGIN_PASSWORD, password)
        self.sl.wait_and_click(MyAccount.LOGIN_BUTTON)