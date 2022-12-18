
from selenium.webdriver.common.by import By


class HomePageLocator:

    CLICK_SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[text()='Samsung galaxy s6']")
    CLICK_NOKIA_LUMIA_1520 = (By.XPATH, "//*[@id='tbodyid']")
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")
    CONTACT_US = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(2) > a")
    CONTACT_EMAIL = (By.CSS_SELECTOR, "#recipient-email")
    CONTACT_NAME = (By.CSS_SELECTOR, "#recipient-name")
    CONTACT_MESSAGE = (By.CSS_SELECTOR, "#message-text")
    SEND_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")
