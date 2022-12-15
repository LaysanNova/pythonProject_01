import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.MyAccount import MyAccount
from blaze.src.helpers.generic_helpers import generate_random_new_user


@pytest.mark.usefixtures("init_driver")
class TestMyAccount:

    @pytest.mark.tcid12
    def test_login_non_existing_user(self):

        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        my_account = MyAccount(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('UserDoesNotExist.')
        my_account.input_login_password('123Abc')
        my_account.click_login_button()
        alert_text = my_account.get_alert_message()
        assert alert_text == 'User does not exist.'

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        pass

        # my_account_new = MyAccount(self.driver)
        # my_account_in = MyAccountSignedIn(self.driver)
        # my_account_new.go_to_my_account()
        #
        # new_user = generate_random_new_user()
        # my_account_new.input_register_username(new_user)
        # my_account_new.input_register_password(new_user)
        # my_account_new.click_register_button()
        #
        # # my_account_in.  verify user is registered