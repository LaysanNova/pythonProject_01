import time

import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestVisual:

    @pytest.mark.tcid100
    def test_carousel(self):

        base_url = get_base_url()
        self.driver.get(base_url)
        main_page = HomePage(self.driver)
        main_page.press_next_carousel()
        time.sleep(2)
        assert main_page.second_slide_is_vsible()
        time.sleep(2)