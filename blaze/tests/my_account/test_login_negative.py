import time

import pytest
from blaze.src.pages.MyAccount import MyAccount


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_non_existing_user(self):

        my_account = MyAccount(self.driver)

        my_account.go_to_my_account()
        my_account.input_login_username('UserDoesNotExist.')
        my_account.input_login_password('123Abc')
        my_account.click_login_button()
        alert_text = my_account.get_alert_message()
        assert alert_text == 'User does not exist.'
