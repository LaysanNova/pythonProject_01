from blaze.src.pages.locators.HomeLocators import HomeLocator
from blaze.src.SeleniumExtended import SeleniumExtended
from blaze.src.helpers.config_helpers import get_base_url


class HomePage(HomeLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def press_next_carousel(self):
        self.sl.wait_and_click(self.B_CAROUSEL_NEXT)

    def press_prev_carousel(self):
        self.sl.wait_and_click(self.B_CAROUSEL_PREV)

    def second_slide_is_vsible(self):
        self.sl.wait_until_element_is_visible(self.IMG_NEXUS)