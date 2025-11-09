from pages.login.login_page import LoginPage
from utilities.test_status import StatusReporter
import unittest
import pytest
import time

@pytest.mark.usefixtures("one_time_setUp", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.sr = StatusReporter(self.driver)

    @pytest.mark.order(5)
    def test_valid_login(self):
        self.lp.login(username="standard_user", password="secret_sauce")
        result1 = self.lp.verify_loginSuccess()
        self.sr.mark_final(test_name="Test Valid Login", result=result1, result_message="Login successful")

    @pytest.mark.order(1)
    def test_locked_login(self):
        result1 = self.lp.verify_pageTitle(title_toVerify="Swag Labs")
        self.sr.mark(result1, result_message="Verify Page Title")
        self.lp.login(username="locked_out_user", password="secret_sauce")
        result2 = self.lp.verify_loginFailed()
        self.sr.mark(result2, result_message="Login Failed")
        result3 = self.lp.check_loginFailed("Epic sadface: Sorry, this user has been locked out.")
        self.sr.mark_final(test_name="Locked Out User Login", result=result3, result_message="Locked Out User Cannot Login")

    @pytest.mark.order(2)
    def test_wrong_login(self):
        self.lp.login(username="standard_user", password="error")
        result1 = self.lp.verify_loginFailed()
        self.sr.mark(result1, result_message="Login Failed")
        result2 = self.lp.check_loginFailed("Epic sadface: Username and password do not match any user in this service")
        self.sr.mark_final(test_name="Wrong Username or Password Login", result=result2,
                           result_message="Cannot Login with Wrong Credentials")

    @pytest.mark.order(3)
    def test_noPass_login(self):
        self.lp.login(username="standard_user", password="")
        result1 = self.lp.verify_loginFailed()
        self.sr.mark(result1, result_message="Login Failed")
        result2 = self.lp.check_loginFailed("Epic sadface: Password is required")
        self.sr.mark_final(test_name="No Password Login", result=result2,
                           result_message="Cannot Login without Password")

    @pytest.mark.order(4)
    def test_noUser_login(self):
        self.lp.login(username="", password="secret_sauce")
        result1 = self.lp.verify_loginFailed()
        self.sr.mark(result1, result_message="Login Failed")
        result2 = self.lp.check_loginFailed("Epic sadface: Username is required")
        self.sr.mark_final(test_name="No User Login", result=result2,
                           result_message="Cannot Login without User")

    @pytest.mark.order(6)
    def test_logout_fail(self):
        self.lp.fail_log_out()
        result1 = self.lp.verify_loginSuccess()
        self.sr.mark_final(test_name="Log Out Failed", result=result1, result_message="Cannot Logout without Side Bar")

    @pytest.mark.order(7)
    def test_logout(self):
        self.lp.logout()
        result1 = self.lp.verify_logoutSuccess()
        self.sr.mark_final(test_name="Log Out Valid", result=result1, result_message="Log Out Successful")

