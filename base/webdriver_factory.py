from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver(self):
        base_url = "https://www.saucedemo.com/"
        if self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            # Set up Firefox as the default browser
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.get(base_url)

        return driver