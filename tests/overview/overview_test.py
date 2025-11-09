from pages.overview.overview_page import OverviewPage
from utilities.test_status import StatusReporter
import unittest
import pytest

@pytest.mark.usefixtures("one_time_setUp", "set_up")
class OverviewTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ow = OverviewPage(self.driver)
        self.sr = StatusReporter(self.driver)

    @pytest.mark.order(20)
    def test_overview(self):
        self.ow.get_to_overview()
        result1 = self.ow.verify_overview()
        self.sr.mark_final(test_name="Getting to overview", result=result1, result_message="Got to overview")

    @pytest.mark.order(21)
    def test_thanks(self):
        self.ow.click_finish()
        result1 = self.ow.verify_completed_order()
        self.sr.mark_final(test_name="Order Completed", result=result1, result_message="Valid Thanks Message")

    @pytest.mark.order(22)
    def test_back_home(self):
        self.ow.click_home()
        result1 = self.ow.verify_home()
        self.sr.mark_final(test_name="Back to Home", result=result1, result_message="Gone Back to Shop")