from selenium.webdriver.common.by import By


class CartPageLocator:

    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "#page-wrapper > div > div.col-lg-1 > button")
    BUTTON_PLACE_ORDER = (By.CSS_SELECTOR, "//button[text()='Place Order']")

    NAME_FIELD = (By.CSS_SELECTOR, "#name")
    COUNTRY_FIELD = (By.CSS_SELECTOR, "#country")
    CITY_FIELD = (By.CSS_SELECTOR, "#city")
    CREDIT_CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.CSS_SELECTOR, "#month")
    YEAR_FIELD = (By.CSS_SELECTOR, "#year")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")
    THANK_YOU_OK_BUTTON = (By.XPATH, "//button[text()='OK']")


    PRODUCTS_IN_CART = (By.CLASS_NAME, "success")

    TOTAL = (By.ID, "totalp")
    BUTTON_DELETE = (By.XPATH, "//a[text()='Delete']")






    # PRODUCTS_IN_CART = (By.ID, "tbodyid")
    PRODUCTS_IN_CART = (By.CLASS_NAME, "success")


