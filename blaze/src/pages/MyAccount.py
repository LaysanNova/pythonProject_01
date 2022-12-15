from blaze.src.pages.locators.MyAccountLocator import MyAccountLocator
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.alert import Alert


class MyAccount(MyAccountLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):

        self.sl.wait_and_click(self.LOGIN_IN)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    # def wait_until_error_is_displayed(self, exp_err):
    #     self.sl.wait_until_element_contains_text(self.ERROR_WARNING, exp_err)

    def input_register_username(self, new_username):
        self.sl.wait_and_input_text(self.REGISTER_USER_NAME, new_username)

    def input_register_password(self, new_password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, new_password)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BUTTON)

    def get_alert_message(self):
        self.sl.wait_alert_window()
        alert_text = Alert(self.driver).text
        Alert(self.driver).accept()
        return alert_text
