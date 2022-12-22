import time

import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.ProductPage import ProductPage


@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    @pytest.mark.tcid100
    def test_can_go_to_page(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.sl.wait_and_check_url_if_matches('https://www.demoblaze.com')

    @pytest.mark.tcid101
    def test_click_on_item(self):

        click_item = HomePage(self.driver)
        click_item.go_to_home_page()
        click_item.sl.wait_and_click(HomePage.CLICK_SAMSUNG_GALAXY_S6)
        click_item.sl.wait_and_check_url_to_be('https://www.demoblaze.com/prod.html?idp_=1')
        click_item.sl.wait_and_click(ProductPage.ADD_TO_CART)
        alert_text = click_item.sl.wait_alert_window().text
        assert alert_text == 'Product added'