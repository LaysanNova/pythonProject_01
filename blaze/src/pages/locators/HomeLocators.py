from selenium.webdriver.common.by import By


class HomeLocator:
    SamsungGalaxyS6 = (By.XPATH, "//a[text()='Samsung galaxy s6']")

    # B_CAROUSEL_NEXT = (By.XPATH, "[data-slide*=next]")
    # B_CAROUSEL_PREV = (By.XPATH, "[data-slide*=prev]")

    B_CAROUSEL_NEXT = (
        By.XPATH, "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/a[2]/span[1]")
    B_CAROUSEL_PREV = (
        By.XPATH, "//span[contains(text(),'Previous')]")
    # FIRST_SLIDE = (By.XPATH, "[alt*=First]")
    # SECOND_SLIDE = (By.CSS_SELECTOR, "[alt*=Second]")
    IMG_SAMSUNG = (By.CSS_SELECTOR, 'img[src*="Samsung1.jpg"]')
    IMG_NEXUS = (By.CSS_SELECTOR, 'img[src*="nexus1.jpg"]')
    IMG_LAPTOP = (By.CSS_SELECTOR, 'img[src*="iphone1.jpg"]')


