from selenium.webdriver.common.by import By


class MyAccountLocator:

    LOGIN_IN = (By.ID, 'login2')

    LOGIN_USER_NAME = (By.ID, 'loginusername')
    LOGIN_PASSWORD = (By.ID, 'loginpassword')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[onclick="logIn()"]')

    REGISTER_USER_NAME = (By.ID, 'sign-username')
    REGISTER_PASSWORD = (By.ID, 'sign-password')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[onclick="register()"]')



