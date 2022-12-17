import time

import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.MyAccount import MyAccount
from blaze.src.helpers.generic_helpers import generate_random_new_user
from blaze.src.helpers.read_data import get_data_from_file
from blaze.src.helpers.print_data import printing_data


@pytest.mark.usefixtures("init_driver")
class TestMyAccount:

    @pytest.mark.tcid1001
    def test_login_non_existing_user(self):

        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        my_account = MyAccount(self.driver)
        my_account.sl.wait_and_click(my_account.LOGIN_IN)
        my_account.sl.wait_and_input_text(MyAccount.LOGIN_USER_NAME, 'UserDoesNotExist.')
        my_account.sl.wait_and_input_text(MyAccount.LOGIN_PASSWORD, '123Abc')
        my_account.sl.wait_and_click(MyAccount.LOGIN_BUTTON)
        alert_text = my_account.sl.wait_alert_window().text
        assert alert_text == 'User does not exist.'

    @pytest.mark.tcid1002
    def test_register_valid_new_user(self):

        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        my_account_new = MyAccount(self.driver)
        my_account_new.sl.wait_and_click(MyAccount.REGISTER_UP)

        new_user = generate_random_new_user()
        my_account_new.sl.wait_and_input_text(MyAccount.REGISTER_USER_NAME, new_user.get('username'))
        my_account_new.sl.wait_and_input_text(MyAccount.REGISTER_PASSWORD, new_user.get('password'))

        # # Test works, but let's not use it, we don't want to create a bunch of users.
        # my_account_new.sl.wait_and_click(MyAccount.REGISTER_BUTTON)
        # alert_text = my_account.sl.wait_alert_window().text
        # assert alert_text == 'Sign up successful.', 'Wrong error'

    @pytest.mark.tcid1003
    def test_login_valid_user(self):

        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        my_account = MyAccount(self.driver)

        valid_user = get_data_from_file(section='ValidUser1', key='username')
        valid_pass = get_data_from_file(section='ValidUser1', key='password')

        my_account.go_to_my_account(valid_user, valid_pass)
        my_account.sl.wait_until_element_is_visible(MyAccount.LOG_OUT)


