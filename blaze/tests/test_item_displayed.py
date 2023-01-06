import time

import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.locators.HomePageLocator import HomePageLocator
from blaze.src.pages.locators.CartPageLocator import CartPageLocator


@pytest.mark.usefixtures("init_driver")
class TestItemDisplayed:
    @pytest.mark.tcid103
    def test_footer_displayed(self):
        driver = HomePage(self.driver)
        driver.go_to_home_page()
        element = driver.sl.wait_until_element_is_visible(HomePage.FOOTER)
        assert element, "Footer is not displayed"
