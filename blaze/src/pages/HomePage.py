from selenium.webdriver.common import alert
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url

from blaze.src.helpers.generic_helpers import get_random_product_from_list
from selenium.webdriver.common.alert import Alert
from selenium.common import TimeoutException
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

    def find_elements(self, locator):

        products = self.sl.wait_until_elements_are_visible(locator)
        product_list = []
        for product in products:
            product_list.append(product.text)
        return product_list

    def add_product_in_cart(self):
        try:
            products = self.find_elements(HomePage.ITEM_NAME)
            random_product = get_random_product_from_list(products)
            locator = self.generate_item_locator(random_product.get('name'))
            self.sl.wait_and_click(locator)
            self.sl.wait_and_click(HomePage.ADD_TO_CART)

            alert_text = self.sl.wait_alert_window().text
            assert alert_text == 'Product added'
            alert_window = Alert(self.driver)
            alert_window.accept()

            return random_product.get('name')

        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")