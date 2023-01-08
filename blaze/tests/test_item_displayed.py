import time

import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.locators.SamsungGalaxyS6Locator import SamsungGalaxyS6Page
from blaze.src.pages.locators.CartPageLocator import CartPageLocator


@pytest.mark.usefixtures("init_driver")
class TestItemDisplayed:
    @pytest.mark.tcid103
    def test_footer_displayed(self):
        driver = HomePage(self.driver)
        driver.go_to_home_page()
        element = driver.sl.wait_until_element_is_visible(HomePage.FOOTER)
        assert element, "Footer is not displayed"

    @pytest.mark.tcid110
    def test_copyright_displayed_flow(self):
        driver = HomePage(self.driver)
        driver.go_to_home_page()
        element = driver.sl.wait_until_element_is_visible(HomePage.COPYRIGHT)
        assert element, "Copyright is not displayed"
        driver.sl.wait_and_click(HomePage.CLICK_SAMSUNG_GALAXY_S6)
        assert element, "Copyright is not displayed"
        driver.sl.wait_and_click(SamsungGalaxyS6Page.SAMSUNG_GALAXY_S6_ADD_TO_CART)
        driver.sl.wait_alert_window()
        alert = driver.switch_to.Alert
        alert.accept(self)
        driver.sl.wait_and_click(SamsungGalaxyS6Page.SAMSUNG_GALAXY_S6_CART_ICON)
        assert element, "Copyright is not displayed"
        driver.sl.wait_and_click(CartPageLocator.PLACE_ORDER_BUTTON)
        driver.sl.wait_and_input_text(CartPageLocator.NAME_FIELD, "John Smith")
        driver.sl.wait_and_input_text(CartPageLocator.CREDIT_CARD_FIELD, "55555555")
        driver.sl.wait_and_click(CartPageLocator.PURCHASE_BUTTON)
        driver.sl.wait_and_click(CartPageLocator.THANK_YOU_OK_BUTTON)
        assert element, "Copyright is not displayed"



