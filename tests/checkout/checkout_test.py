from pages.checkout.checkout_page import CheckoutPage
from pages.cart.cart_page import CartPage
from utilities.test_status import StatusReporter
import unittest
import pytest

@pytest.mark.usefixtures("one_time_setUp", "set_up")
class CheckOutTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.chp= CheckoutPage(self.driver)
        self.sr = StatusReporter(self.driver)
        self.cp = CartPage(self.driver)

    @pytest.mark.order(16)
    def test_checkout(self):
        self.chp.checkout()
        result1 = self.chp.verify_checkout()
        self.sr.mark_final(test_name="Checkout Successful", result=result1, result_message="Checkout ready")

    @pytest.mark.order(17)
    def test_checkout_error(self):
        result1 = self.chp.verify_checkout_error(expected_text="Error: First Name is required")
        self.sr.mark(result=result1,result_message="First Name Error Displayed Correctly")
        result2 = self.chp.verify_checkout_error(first_name="Test",expected_text="Error: Last Name is required")
        self.sr.mark(result=result2, result_message="Last Name Error Displayed Correctly")
        result3 = self.chp.verify_checkout_error(first_name="Test", last_name="Auto",
                                                 expected_text="Error: Postal Code is required")
        self.sr.mark_final(test_name="Wrong information",result=result3,
                           result_message="Postal Code Error Displayed Correctly")

    @pytest.mark.order(18)
    def test_back_to_cart(self):
        self.chp.click_cancel()
        result1 = self.cp.verify_added_item()
        self.sr.mark(result1, result_message="Cancel returns to Cart")
        self.chp.click_checkout()
        self.chp.click_shopping_cart()
        result2 = self.cp.verify_added_item()
        self.sr.mark_final(test_name="Back to Cart", result=result2, result_message="Shopping Cart returns to Cart")

    @pytest.mark.order(19)
    def test_complete_checkout(self):
        self.chp.click_checkout()
        self.chp.complete_checkout(first_name="Test", last_name="Auto", postal_code="49668")
        result1 = self.chp.verify_checkout_completed()
        self.sr.mark_final(test_name="Checkout Overivew", result=result1, result_message="Checkout Info Added")
