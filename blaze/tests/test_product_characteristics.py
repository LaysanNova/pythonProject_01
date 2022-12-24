import time
import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.helpers.print_data import printing_data


@pytest.mark.usefixtures("init_driver")
class TestCharacteristicsByCategories:

    @pytest.mark.tcid3000
    @pytest.mark.parametrize(
        "locator_categories",
        [
            pytest.param(
                HomePage.PHONES,
                marks=pytest.mark.phones,
                id="Phones"
            ),
            pytest.param(
                HomePage.LAPTOPS,
                marks=pytest.mark.laptops,
                id="Laptops"
            ),
            pytest.param(
                HomePage.MONITORS,
                marks=pytest.mark.monitors,
                id="Monitors"
            ),
        ],
    )
    def test_product_has_name_price_description(self, locator_categories):
        products = HomePage(self.driver)
        products.go_to_home_page()
        products.sl.wait_and_click(locator_categories)
        prod_list = products.get_list_of_products(HomePage.ITEM_BLOCK)
        for i in range(len(prod_list)):
            prod_data = prod_list[i].replace("$", "").split("\n")
            assert prod_data[0] != '', 'Product has no name.'
            assert int(prod_data[1]) > 0, 'Product has no price.'
            assert len(prod_data[2]) > 0, 'Product has no description.'
