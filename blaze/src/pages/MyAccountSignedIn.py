from blaze.src.SeleniumExtended import SeleniumExtended


class MuAccountSignedIn:

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # def VERIFY  user is signed in