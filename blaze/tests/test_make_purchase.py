import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.locators.HomePageLocator import HomePageLocator


@pytest.mark.usefixtures("init_driver")
class MakePurchaseEndToEnd:

    @pytest.mark.tcid3000
    def test_make_purchase_end_to_end(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.sl.wait_and_click(HomePageLocator.CLICK_SAMSUNG_GALAXY_S6)
        home_page.sl.wait_and_check_url_to_be('https://www.demoblaze.com/prod.html?idp_=1')
        home_page.sl.wait_and_click(HomePage.ADD_TO_CART)
        alert_text = home_page.sl.wait_alert_window().text
        assert alert_text in 'Product added'

