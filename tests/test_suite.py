import unittest
from tests.login.login_test import LoginTests
from tests.shop.shop_test import ShopTests
from tests.cart.cart_test import CartTests
from tests.checkout.checkout_test import CheckOutTests
from tests.overview.overview_test import OverviewTests

# Test Cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ShopTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CartTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(CheckOutTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(OverviewTests)

# Create the test suite
test_suite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])

unittest.TextTestRunner(verbosity=2).run(test_suite)