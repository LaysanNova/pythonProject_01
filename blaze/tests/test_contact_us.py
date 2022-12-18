import pytest

from blaze.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestMakePurchase:
    @pytest.mark.tcid106
    def test_contact_us(self):
        contact_us = HomePage(self.driver)
        contact_us.go_to_home_page()
        contact_us.sl.wait_and_click(HomePage.CONTACT_US)
        contact_us.sl.wait_and_input_text(HomePage.CONTACT_EMAIL, "JohnSmith@gmail.com")
        contact_us.sl.wait_and_input_text(HomePage.CONTACT_NAME, "John Smith")
        contact_us.sl.wait_and_input_text(HomePage.CONTACT_MESSAGE, "I want a new phone")
        contact_us.sl.wait_and_click(HomePage.SEND_MESSAGE)
        alert_text = contact_us.sl.wait_alert_window().text
        assert alert_text in 'Thanks for the message!!'
