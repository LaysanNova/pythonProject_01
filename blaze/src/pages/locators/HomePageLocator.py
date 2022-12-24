
from selenium.webdriver.common.by import By


class HomePageLocator:

    HOME_PAGE = (By.XPATH, "//a[text()='Home ']")
    CLICK_SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[text()='Samsung galaxy s6']")
    CLICK_NOKIA_LUMIA_1520 = (By.XPATH, "//*[@id='tbodyid']")
    BLOCK_NOKIA_LUMIA_1520 = (By.XPATH, "//div[@class ='card h-100']")

    # 9 items on page, Phones 7, Laptops 6, Monitors 2, Total 15
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    CONTACT_US = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(2) > a")
    CONTACT_EMAIL = (By.CSS_SELECTOR, "#recipient-email")
    CONTACT_NAME = (By.CSS_SELECTOR, "#recipient-name")
    CONTACT_MESSAGE = (By.CSS_SELECTOR, "#message-text")
    SEND_MESSAGE_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")
    
    PHONES = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS = (By.XPATH, "//a[text()='Laptops']")
    MONITORS = (By.XPATH, "//a[text()='Monitors']")

    ITEM_NAME = (By.CLASS_NAME, 'hrefch')
    ITEM_BLOCK = (By.CLASS_NAME, 'card-block')

    CART_HEADER = (By.ID, "cartur")
    CART_ON_CART_PAGE = (By.CSS_SELECTOR, "a[onclick='showcart()']")

    CART = (By.XPATH, "//a[text()='Cart']")
    FOOTER = (By.CSS_SELECTOR, "body > footer > p")
    CLICK_PRODUCT_STORE = (By.CSS_SELECTOR, "#nava")

    def generate_item_locator(self, text):
        ITEM_NAME_GENERATED = (By.XPATH, "//a[text()=" + "'" + text + "'" + "]")
        return ITEM_NAME_GENERATED

