import time

import pytest
from blaze.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    @pytest.mark.tcid100
    def test_can_go_to_page(self):

        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.sl.wait_and_check_url_if_matches('https://www.demoblaze.com')

    @pytest.mark.tcid101
    def test_click_on_item(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.click_on_item()






