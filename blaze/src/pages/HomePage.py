from selenium.webdriver.common import alert
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url
from blaze.src.pages.locators.HomePageLocator import HomePageLocator
import logging


class HomePage(HomePageLocator):
    LOGGER = logging.getLogger(__name__)

    def __init__(self, driver):
        self.switch_to = alert
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        base_url = get_base_url()
        self.driver.get(base_url)

    def get_list_of_products(self, locator):
        products = self.sl.wait_until_elements_are_visible(locator, 3)
        product_list = []
        for product in products:
            product_list.append(product.text)
        return product_list

