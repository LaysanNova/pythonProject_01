from blaze.src.pages.locators.ProductPageLocator import ProductPageLocator
from blaze.src.SeleniumExtended import SeleniumExtended


class ProductPage(ProductPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
