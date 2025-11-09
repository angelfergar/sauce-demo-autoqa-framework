import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from utilities.util import Util

class CartPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)
    utils = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _checkout_button = "checkout" # ID
    _first_item = "cart_item" # class
    _first_item_name = "//div[@class='inventory_item_name'][1]"
    _remove_button = "btn.btn_secondary.btn_small.cart_button" # class
    _continue_button = "continue-shopping" # ID
    _side_menu = "react-burger-menu-btn" # ID
    _all_item_btn = "inventory_sidebar_link" # ID
    _filter = "product_sort_container"  # class

    # Methods to perform actions on the web
    def get_item_text(self):
        return self.get_text(self._first_item_name)

    def remove_item(self):
        self.element_click(self._remove_button, locator_type="class")

    def click_continue(self):
        self.element_click(self._continue_button, locator_type="id")

    def click_all_items(self):
        self.wait_for_element(self._checkout_button, locator_type="id")
        self.element_click(self._side_menu, locator_type="id")
        self.wait_for_element(self._all_item_btn, locator_type="id")
        self.element_click(self._all_item_btn, locator_type="id")

    def get_item_list(self):
        item_list = self.get_elementList(self._first_item, locator_type="class")
        return item_list

    # Methods to verify the information of the cart
    def verify_added_item(self):
        self.wait_for_element(self._checkout_button, locator_type="ID")
        result = self.isElement_present(self._checkout_button, locator_type="ID")
        return result

    def verify_remove_btn(self):
        item = self.get_element(self._first_item, locator_type="class")
        button = self.get_element_child(item, locator=self._remove_button, locator_type="class")
        result = self.isElement_present(element=button)
        return result

    def verify_shop(self):
        self.wait_for_element(self._filter, locator_type="class")
        result = self.isElement_present(self._filter, locator_type="class")
        return result