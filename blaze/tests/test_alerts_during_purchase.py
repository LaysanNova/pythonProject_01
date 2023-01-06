
import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.locators.SamsungGalaxyS6Locator import SamsungGalaxyS6Page
from blaze.src.pages.locators.CartPageLocator import CartPageLocator


@pytest.mark.usefixtures("init_driver")
class TestPurchaseAlert:

    @pytest.mark.tcid1030
    def test_name_and_credit_card_required(self):
        samsung = HomePage(self.driver)
        samsung.go_to_home_page()
        samsung.sl.wait_and_click(HomePage.CLICK_SAMSUNG_GALAXY_S6)
        samsung.sl.wait_and_click(SamsungGalaxyS6Page.SAMSUNG_GALAXY_S6_ADD_TO_CART)
        samsung.sl.wait_alert_window()
        alert = samsung.switch_to.Alert
        alert.accept(self)
        samsung.sl.wait_and_click(SamsungGalaxyS6Page.SAMSUNG_GALAXY_S6_CART_ICON)
        samsung.sl.wait_and_click(CartPageLocator.PLACE_ORDER_BUTTON)
        samsung.sl.wait_and_click(CartPageLocator.PURCHASE_BUTTON)
        alert_text = samsung.sl.wait_alert_window().text
        assert alert_text in 'Please fill out Name and Creditcard.'



