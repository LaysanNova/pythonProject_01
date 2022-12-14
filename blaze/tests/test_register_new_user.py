import pytest
from blaze.src.pages.MyAccount import MyAccount
from blaze.src.pages.MyAccountSignedIn import MuAccountSignedIn
from blaze.src.helpers.generic_helpers import generate_random_new_user


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

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









