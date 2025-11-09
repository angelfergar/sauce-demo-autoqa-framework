import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from utilities.util import Util

class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)
    utils = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "user-name" # ID
    _password_field = "password" # ID
    _login_button = "login-button" # ID
    _login_failed = "//h3[@data-test='error']"
    _shopping_cart = "//a[@class='shopping_cart_link']"
    _side_button = "react-burger-menu-btn" # ID
    _logout_button = "logout_sidebar_link" # ID

    # Actions needed to log in or log out
    def enter_username(self, username):
        self.send_keys(username, self._username_field, locator_type="id")
    def enter_password(self, password):
        self.send_keys(password, self._password_field, locator_type="id")
    def click_login(self):
        self.element_click(self._login_button, locator_type="id")
    def click_sidebar(self):
        self.element_click(self._side_button, locator_type="id")
    def click_logout(self):
        self.element_click(self._logout_button, locator_type="id")

    # Method to execute the login process
    def login(self, username = "", password = ""):
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Methods to verify the logins
    def verify_loginSuccess(self):
        self.wait_for_element(self._shopping_cart, condition="click")
        result = self.isElement_present(self._shopping_cart)
        return result

    def verify_loginFailed(self):
        self.wait_for_element(self._login_failed, condition="present")
        result = self.isElement_present(self._login_failed)
        return result

    def check_loginFailed(self, expected_text =""):
        login_reason = self.get_text(self._login_failed)
        text_check = self.util.verify_text_contains(login_reason, expected_text)
        return text_check

    def clear_fields(self):
        self.wait_for_element(self._username_field,locator_type="id", condition="click")
        username_field = self.get_element(self._username_field, locator_type="id")
        password_field = self.get_element(self._password_field, locator_type="id")
        username_field.clear()
        password_field.clear()

    # Method to click the log out button without having the side menu displayed
    def fail_log_out(self):
        self.click_logout()

    # Log Out Method
    def logout(self):
        self.click_sidebar()
        self.click_logout()

    def verify_logoutSuccess(self):
        self.wait_for_element(self._login_button, locator_type="id", condition="click")
        result = self.isElement_present(self._login_button, locator_type="id")
        return result






