import time
import pytest
from blaze.src.pages.HomePage import HomePage
from blaze.src.pages.CartPage import CartPage
from blaze.src.pages.ProductPage import ProductPage
from blaze.src.helpers.print_data import printing_data
from blaze.src.helpers.generic_helpers import get_random_product_from_list


@pytest.mark.usefixtures("init_driver")
class TestMakeItemPurchase:

    @pytest.mark.tcid3000
    def test_check_prices_and_total_amount(self):

        # Checking if price is displayed on the pages Home and Product
        page_item = HomePage(self.driver)
        page_item.go_to_home_page()
        price_on_home_page = page_item.sl.wait_until_element_is_visible(HomePage.BLOCK_NOKIA_LUMIA_1520).text
        price_on_home_page = int(price_on_home_page.split('\n')[1].replace('$', ''))
        assert price_on_home_page > 0, 'Price in main page is not placed.'

        page_item.sl.wait_and_click(HomePage.BLOCK_NOKIA_LUMIA_1520)

        page_product = ProductPage(self.driver)
        price_on_product_page = page_product.sl.wait_until_element_is_visible(ProductPage.PRICE_CONTAINER).text
        price_on_product_page = int(price_on_product_page.split(' ')[0].replace('$', ''))
        assert price_on_home_page == price_on_product_page, 'Price on product page is not placed.'

        # Checking if price and total amount are correct with one product in the cart
        page_product.add_product_in_cart()
        page_product.sl.wait_and_click(ProductPage.CART)

        page_cart = CartPage(self.driver)
        price_on_cart_page = page_cart.sl.wait_until_element_is_visible(CartPage.PRODUCTS_IN_CART).text
        price_on_cart_page = page_cart.get_product_price(price_on_cart_page)

        assert price_on_product_page == price_on_cart_page, 'Price in the cart is not placed.'

        total = int(page_cart.sl.wait_until_element_is_visible(CartPage.TOTAL).text)

        assert price_on_product_page == total, 'Total price is not correct.'

        # Checking if price and total amount are correct with two products in the cart
        page_cart.sl.wait_and_click(HomePage.HOME_PAGE)

        products = page_item.get_list_of_products(HomePage.ITEM_NAME)
        random_product = get_random_product_from_list(products)
        locator = page_item.generate_item_locator(random_product.get('name'))
        page_item.sl.wait_and_click(locator)

        price_on_product_page = page_product.sl.wait_until_element_is_visible(ProductPage.PRICE_CONTAINER).text
        price_on_product_page = int(price_on_product_page.split(' ')[0].replace('$', ''))
        assert price_on_product_page, 'Price on product page is not placed.'

        page_product.add_product_in_cart()
        page_product.sl.wait_and_click(ProductPage.CART)

        page_cart = CartPage(self.driver)
        product_list = page_item.get_list_of_products(CartPage.PRODUCTS_IN_CART)

        sum_of_products_price = sum(list(map(page_cart.get_product_price, product_list)))
        total = int(page_cart.sl.wait_until_element_is_visible(CartPage.TOTAL).text)
        assert sum_of_products_price == total, "Total price does not match to sum of the product's items."

        # Checking if total amount as correct after removing product from the cart
        page_cart.sl.wait_and_click(CartPage.BUTTON_DELETE)

        product_list = page_item.get_list_of_products(CartPage.PRODUCTS_IN_CART)

        sum_of_products_price = sum(list(map(page_cart.get_product_price, product_list)))
        total = int(page_cart.sl.wait_until_element_is_visible(CartPage.TOTAL).text)
        assert sum_of_products_price == total, "Total price does not match to sum of the product's items."












