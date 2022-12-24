from blaze.src.pages.locators.ProductPageLocator import ProductPageLocator
from blaze.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.alert import Alert


class ProductPage(ProductPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def add_product_in_cart(self):
        self.sl.wait_and_click(ProductPage.ADD_TO_CART)

        alert_text = self.sl.wait_alert_window().text
        assert alert_text == 'Product added'
        alert_window = Alert(self.driver)
        alert_window.accept()
