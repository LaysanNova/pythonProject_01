from blaze.src.pages.locators.HomeLocators import HomeLocator
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url


class HomePage(HomeLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)