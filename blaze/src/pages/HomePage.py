from blaze.src.pages.locators.HomePageLocator import HomePageLocator
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url


class HomePage(HomePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        base_url = get_base_url()
        self.driver.get(base_url)
