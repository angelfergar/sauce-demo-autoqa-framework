import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.shop.shop_page import ShopPage
from pages.cart.cart_page import CartPage
from utilities.util import Util

class CheckoutPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)
    utils = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lp = LoginPage(self.driver)
        self.sp = ShopPage(self.driver)
        self.cp = CartPage(self.driver)

    # Locators
    _checkout_button = "checkout" # ID
    _info_form = "first-name" # ID
    _continue_button ="continue" # ID
    _error_reason = "//h3[@data-test='error']"
    _first_name = "first-name" # ID
    _last_name = "last-name" # ID
    _postal_code = "postal-code" # ID
    _cancel_button = "cancel" # ID
    _shopping_cart = "shopping_cart_link"  # class
    _summary_info = "summary_info" # class

    # Methods to perform actions on the web
    def click_checkout(self):
        self.wait_for_element(self._checkout_button, locator_type="id")
        self.element_click(self._checkout_button, locator_type="id")

    def click_continue(self):
        self.element_click(self._continue_button, locator_type="id")

    def click_cancel(self):
        self.element_click(self._cancel_button, locator_type="id")

    def click_shopping_cart(self):
        self.element_click(self._shopping_cart, locator_type="class")

    def send_first_name(self, message):
        self.send_keys(message=message, locator=self._first_name, locator_type="id")

    def send_last_name(self, message):
        self.send_keys(message=message, locator=self._last_name, locator_type="id")

    def send_postal_code(self, message):
        self.send_keys(message=message, locator=self._postal_code, locator_type="id")

    def checkout(self):
        self.lp.login(username="standard_user", password="secret_sauce")
        self.sp.add_one_item()
        self.sp.click_cart_button()
        self.click_checkout()

    def complete_checkout(self, first_name, last_name, postal_code):
        self.wait_for_element(self._info_form, locator_type="id")
        self.send_first_name(first_name)
        self.send_last_name(last_name)
        self.send_postal_code(postal_code)
        self.click_continue()

    # Methods to verify the information of the checkout

    def verify_checkout(self):
        self.wait_for_element(self._info_form, locator_type="id")
        result = self.isElement_present(self._info_form, locator_type="id")
        return result

    def verify_checkout_completed(self):
        self.wait_for_element(self._summary_info, locator_type="class")
        result = self.isElement_present(self._summary_info, locator_type="class")
        return result

    def check_missing_text(self, expected_text):
        error_text = self.get_text(self._error_reason)
        result = self.utils.verify_text_match(error_text, expected_text)
        return result

    def verify_checkout_error(self, first_name ="", last_name ="", postal_code="", expected_text=""):
        self.clear_fields()
        self.send_first_name(first_name)
        self.send_last_name(last_name)
        self.send_postal_code(postal_code)
        self.click_continue()
        result = self.check_missing_text(expected_text=expected_text)
        return result

    def clear_fields(self):
        self.wait_for_element(self._info_form, locator_type="id")
        first_name = self.get_element(self._first_name, locator_type="id")
        last_name = self.get_element(self._last_name, locator_type="id")
        postal_code = self.get_element(self._postal_code, locator_type="id")
        first_name.clear()
        last_name.clear()
        postal_code.clear()

