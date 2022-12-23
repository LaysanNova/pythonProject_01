
from selenium.webdriver.common.by import By


class HomePageLocator:

    HOME_PAGE = (By.XPATH, "//a[text()='Home ']")
    CLICK_SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[text()='Samsung galaxy s6']")
    CLICK_NOKIA_LUMIA_1520 = (By.XPATH, "//*[@id='tbodyid']")

    # 9 items on page, Phones 7, Laptops 6, Monitors 2, Total 15
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    ABOUT_US = (By.XPATH, "//a[contains(text(),'About us')]")
    ABOUT_US_VIDEO = (By.XPATH, "//div[@id='example-video']")
    ABOUT_US_CLOSE = (By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[3]/button[1]")

    CONTACT_US = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(2) > a")
    CONTACT_EMAIL = (By.CSS_SELECTOR, "#recipient-email")
    CONTACT_NAME = (By.CSS_SELECTOR, "#recipient-name")
    CONTACT_MESSAGE = (By.CSS_SELECTOR, "#message-text")
    SEND_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")
    
    PHONES = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS = (By.XPATH, "//a[text()='Laptops']")
    MONITORS = (By.XPATH, "//a[text()='Monitors']")

    ITEM_NAME = (By.CLASS_NAME, 'hrefch')
    ITEM_BLOCK = (By.CLASS_NAME, 'card-block')

    # CART = (By.ID, "cartur")
    # CART1 = (By.CSS_SELECTOR, "a[onclick='showcart()']")
    CART = (By.XPATH, "//a[text()='Cart']")

    def generate_item_locator(self, text):
        ITEM_NAME_GENERATED = (By.XPATH, "//a[text()=" + "'" + text + "'" + "]")
        return ITEM_NAME_GENERATED

