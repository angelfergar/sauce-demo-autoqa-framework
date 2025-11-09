import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from utilities.util import Util
from pages.shop.shop_page import ShopPage
from pages.checkout.checkout_page import CheckoutPage

class OverviewPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)
    utils = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.sp = ShopPage(self.driver)
        self.chp = CheckoutPage(self.driver)

    # Locators
    _item_name = "inventory_item_name" # class
    _finish_button = "finish" # ID
    _thanks_message = "complete-header" # class
    _home_button = "back-to-products" # ID

    # Methods to perform actions on the web

    def click_finish(self):
        self.element_click(self._finish_button, locator_type="id")

    def click_home(self):
        self.element_click(self._home_button, locator_type="id")

    def get_to_overview(self):
        self.chp.checkout()
        self.chp.complete_checkout(first_name="Test", last_name="Auto", postal_code="49668")

    # Methods to verify the information of the checkout

    def verify_overview(self):
        self.wait_for_element(self._item_name, locator_type="class")
        result = self.isElement_present(self._item_name, locator_type="class")
        return result

    def verify_completed_order(self):
        self.wait_for_element(self._thanks_message, locator_type="class")
        thanks_text = self.get_text(self._thanks_message, locator_type="class")
        complete_text = "Thank you for your order!"
        result = self.utils.verify_text_match(thanks_text, complete_text)
        return result

    def verify_home(self):
        result = self.sp.verify_list_length()
        return result


