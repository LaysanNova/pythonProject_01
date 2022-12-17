import time

import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.locators.SamsungGalaxyS6Locator import SamsungGalaxyS6Page
from blaze.src.pages.locators.HomePageLocator import HomePageLocator
from blaze.src.pages.locators.CartPageLocator import CartPageLocator



@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    @pytest.mark.tcid103
    def test_make_SamsungGalaxyS6_purchase(self):
        purchase = HomePage(self.driver)
        purchase.go_to_home_page()
        purchase.sl.wait_and_click(HomePageLocator.CLICK_SAMSUNG_GALAXY_S6)
        purchase.sl.wait_and_check_url_to_be('https://www.demoblaze.com/prod.html?idp_=1')
        purchase.sl.wait_and_click(SamsungGalaxyS6Page.SAMSUNG_GALAXY_S6_ADD_TO_CART)
        purchase.sl.wait_alert_window()
        alert = purchase.switch_to.Alert
        alert.accept(self)
        purchase.sl.wait_and_click(SamsungGalaxyS6Page.SAMSUNG_GALAXY_S6_CART_ICON)
        purchase.sl.wait_and_click(CartPageLocator.PLACE_ORDER_BUTTON)
        purchase.sl.wait_and_input_text(CartPageLocator.NAME_FIELD, "John Smith")
        purchase.sl.wait_and_input_text(CartPageLocator.COUNTRY_FIELD, "USA")
        purchase.sl.wait_and_input_text(CartPageLocator.CREDIT_CARD_FIELD, "900")
        purchase.sl.wait_and_input_text(CartPageLocator.MONTH_FIELD, "12")
        purchase.sl.wait_and_click(CartPageLocator.YEAR_FIELD, "2022")
        purchase.sl.wait_and_click(CartPageLocator.PURCHASE_BUTTON)
        purchase.sl.wait_and_click(CartPageLocator.THANK_YOU_OK_BUTTON)





