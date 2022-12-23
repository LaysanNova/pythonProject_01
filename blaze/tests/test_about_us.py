import pytest

from blaze.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestContactUs:
    @pytest.mark.tcid106
    def test_video_about_us_is_present(self):
        homePage = HomePage(self.driver)
        homePage.go_to_home_page()
        homePage.sl.wait_and_click(HomePage.ABOUT_US)
        assert homePage.sl.wait_until_element_is_visible(HomePage.ABOUT_US_VIDEO)
        homePage.sl.wait_and_click(homePage.ABOUT_US_CLOSE)
        assert homePage.sl.wait_until_element_is_visible(homePage.HOME_PAGE)
