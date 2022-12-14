# import time
#
# import pytest
# from blaze.src.pages.HomePage import HomePage
# from blaze.src.helpers.config_helpers import get_base_url
#
#
# @pytest.mark.usefixtures("init_driver")
# class Test_1:
#
#     @pytest.mark.tcid100
#     def test_add(self):
#
#         base_url = get_base_url()
#         self.driver.get(base_url)
#         my_account = HomePage(self.driver)
#         time.sleep(10)
#
#         my_account.add_item_to_cart()
#         time.sleep(10)
#
#
# #       assert alert_text == 'User does not exist.'