from pages.shop.shop_page import ShopPage
from pages.login.login_page import LoginPage
from utilities.test_status import StatusReporter
import unittest
import pytest

@pytest.mark.usefixtures("one_time_setUp", "set_up")
class ShopTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.sp = ShopPage(self.driver)
        self.sr = StatusReporter(self.driver)

    @pytest.mark.order(8)
    def test_check_list(self):
        self.lp.login(username="standard_user", password="secret_sauce")
        result1 = self.sp.verify_list_length()
        self.sr.mark(result1, result_message="List's length checked")
        result2 = self.sp.verify_list_titles()
        self.sr.mark(result2, result_message="List's names checked")
        result3 = self.sp.verify_list_descs()
        self.sr.mark(result3, result_message="List's descriptions checked")
        result4 = self.sp.verify_list_prices()
        self.sr.mark_final(test_name="Test Inventory List", result=result4, result_message="List's prices checked")

    @pytest.mark.order(9)
    def test_sort_filter(self):
        result1 = self.sp.verify_title_order()
        self.sr.mark(result=result1, result_message="Titles sorted from A to Z")
        self.sp.sort_title_asc()
        result2 = self.sp.verify_title_order(sorting="asc")
        self.sr.mark(result=result2, result_message="Titles sorted from Z to A")
        self.sp.sort_price_desc()
        result3 = self.sp.verify_price_order("desc")
        self.sr.mark(result=result3, result_message="Prices sorted from High to Low")
        self.sp.sort_price_asc()
        result4 = self.sp.verify_price_order()
        self.sr.mark_final(test_name="Item Sorting", result=result4, result_message="Prices sorted from Low to High")

    @pytest.mark.order(10)
    def test_add_button(self):
        result1 = self.sp.verify_add_button()
        self.sr.mark_final(test_name="Add Button Present", result=result1, result_message="Every Item has a Add to "
                                                                                          "Cart Button")

    @pytest.mark.order(11)
    def test_add_item(self):
        self.sp.click_add_item()
        result1 = self.sp.verify_added_items(quantity=6)
        self.sr.mark(result=result1, result_message="All items have been added to cart")
        result2 = self.sp.verify_remove_button()
        self.sr.mark_final(test_name="Add Items to Cart", result=result2, result_message="Every Add Button is now "
                                                                                         "a Removed Button")

    @pytest.mark.order(12)
    def test_remove_item(self):
        self.sp.click_remove_button()
        result1 = self.sp.verify_removed_items
        self.sr.mark_final(test_name="Remove Items from Cart", result=result1, result_message="All items have been "
                                                                                               "removed")

