from base.selenium_driver import SeleniumDriver
from utilities.util import Util

class BasePage(SeleniumDriver):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_pageTitle(self, title_toVerify):
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_toVerify)
        except:
            self.log.error("Failed to get page title")
            return False

