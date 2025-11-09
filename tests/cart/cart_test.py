from pages.shop.shop_page import ShopPage
from pages.login.login_page import LoginPage
from pages.cart.cart_page import CartPage
from utilities.test_status import StatusReporter
from utilities.util import Util
import unittest
import pytest

@pytest.mark.usefixtures("one_time_setUp", "set_up")
class CartTests(unittest.TestCase):
    utils = Util()

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.sp = ShopPage(self.driver)
        self.cp = CartPage(self.driver)
        self.sr = StatusReporter(self.driver)

    @pytest.mark.order(13)
    def test_one_item(self):
        self.lp.login(username="standard_user", password="secret_sauce")
        self.sp.add_one_item()
        first_item_text = self.sp.get_item_text()
        self.sp.click_cart_button()
        result1 = self.cp.verify_added_item()
        first_cart_text = self.cp.get_item_text()
        self.sr.mark(result=result1, result_message="Access to Cart Page Correct")
        result2 = self.utils.verify_text_match(first_cart_text, first_item_text)
        self.sr.mark(result=result2, result_message="Item in the cart matches selected in Shop")
        result3 = self.cp.verify_remove_btn()
        self.sr.mark_final(test_name="Add Item to Cart", result=result3, result_message="Item has Remove Button")

    @pytest.mark.order(14)
    def test_remove_item(self):
        self.cp.remove_item()
        item_list = self.cp.get_item_list()
        result1 = self.utils.verify_list_length([], item_list)
        self.sr.mark_final(test_name="Remove Item from Cart", result=result1, result_message="Item removed")

    @pytest.mark.order(15)
    def test_continue_shopping(self):
        self.cp.click_continue()
        result1 = self.cp.verify_shop()
        self.sr.mark(result=result1, result_message="Back to Shop with Continue Shopping")
        self.sp.click_cart_button()
        self.cp.click_all_items()
        result2 = self.cp.verify_shop()
        self.sr.mark_final(test_name="Back to Shop", result=result2, result_message="Back to Shop with All Items")





