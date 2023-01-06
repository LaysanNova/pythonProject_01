from selenium.webdriver.common.by import By


class ProductPageLocator:

    CART = (By.XPATH, "//a[text()='Cart']")
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    PRICE_CONTAINER = (By.XPATH, '//h3[@class="price-container"]')
