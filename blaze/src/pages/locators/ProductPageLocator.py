from selenium.webdriver.common.by import By


class ProductPageLocator:
    # CART = (By.ID, "cartur")
    # CART = (By.CSS_SELECTOR, "a[onclick='showcart()']")
    CART = (By.XPATH, "//a[text()='Cart']")
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")