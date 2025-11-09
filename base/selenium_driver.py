from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # Get page's title
    def get_title(self):
        return self.driver.title

    # We use this method to select what type of By we use
    def get_byType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "css":
            return By.CSS_SELECTOR
        else:
            self.log.debug(f"Locator type: {locator_type} not found")
        return False

    # This is the generic method used to find elements in the web
    def get_element(self, locator, locator_type="xpath", element=None):
        try:
            locator_type = locator_type.lower()
            byType = self.get_byType(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.debug(f"Element found with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(f"Element not found with locator: {locator} and locatorType: {locator_type}")
        return element

    # This is the generic method used to find lists of elements that share the same locator
    def get_elementList(self, locator, locator_type="xpath", element_list=None):
        try:
            locator_type = locator_type.lower()
            byType = self.get_byType(locator_type)
            element_list = self.driver.find_elements(byType, locator)
            self.log.debug(f"Element list found with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(f"Element list not found with locator: {locator} and locatorType: {locator_type}")
        return element_list

    def get_element_child(self, parent_element, locator, locator_type="xpath", element=None):
        try:
            locator_type = locator_type.lower()
            byType = self.get_byType(locator_type)
            element = parent_element.find_element(byType, locator)
            self.log.debug(f"Child element found with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(f"Child element not found with locator: {locator} and locatorType: {locator_type}")
        return element

    # Generic method for clicking elements in the web
    def element_click(self, locator=None, locator_type="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f"Clicked on element with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(f"Could not click on element with locator: {locator} and locatorType: {locator_type}")

    # Generic method for sending data to elements in the web
    def send_keys(self, message, locator, locator_type="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(message)
            self.log.info(f"Sent {message} to element with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(
                f"Could not send {message} to element with locator: {locator} and locatorType: {locator_type}")

    # Generic method to obtain the text from the elements in the web
    def get_text(self, locator=None, locator_type="xpath", element=None):
        text = ""
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            self.log.debug(f"After finding element, size is: {str(len(text))}")
            if len(text) == 0:
                text = element.get_attribute("innerText")
                text = text.strip()
            if text:
                self.log.info(f"The text in the element is: {text}")
            else:
                self.log.debug(f"Element had no visible text.")
        except:
            self.log.error(f"Failed to get the text in the element with locator: {locator} and locatorType: {locator_type}")
            text = None
        return text

    # Generic method to obtain the text from a list of elements
    def get_elementsText(self, locator, locator_type="xpath", element_list=None):
        texts = []
        try:
            if locator:
                element_list = self.get_elementList(locator, locator_type)
                for element in element_list:
                    text = element.text
                    if len(text) == 0:
                        text = element.get_attribute("innerText")
                        text = text.strip()
                    if text:
                        self.log.info(f"The text in the element is: {text}")
                    else:
                        self.log.debug(f"Element had no visible text.")
                    texts.append(text)
                self.log.info(f"Got {len(element_list)} elements with texts: {texts} ")
        except:
            self.log.error(f"Failed to get the texts in the element list with locator: {locator} and locatorType: {locator_type}")
            texts = []
        return texts

    # Generic method to check if an element is present on a web (Useful for explicit waits)
    def isElement_present(self, locator=None, locator_type="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.debug(f"Element present with locator: {locator} and locatorType: {locator_type}")
                return True
            else:
                self.log.error(f"Element not present with locator: {locator} and locatorType: {locator_type}")
                return False
        except:
            self.log.error(f"Element not present with locator: {locator} and locatorType: {locator_type}")
            return False

    # Generic method to check if a list of elements are present on a web (Useful for explicit waits)
    def isElementList_present(self, locator, locator_type="xpath", element_list=None):
        try:
            if locator:
                element_list = self.get_elementList(locator, locator_type)
            if element_list > 0:
                self.log.debug(f"Element list present with locator: {locator} and locatorType: {locator_type}")
                return True
            else:
                self.log.error(f"Element not present with locator: {locator} and locatorType: {locator_type}")
                return False
        except:
            self.log.error(f"Element not present with locator: {locator} and locatorType: {locator_type}")

    # Generic method to check if an element is visible in the web
    def isElement_displayed(self, locator, locator_type="xpath", element=None):
        is_displayed = False
        try:
            if locator:
                element = self.get_elementList(locator, locator_type)
                if element is not None:
                    is_displayed = element.is_displayed()
                    self.log.debug(f"Element displayed with locator: {locator} and locatorType: {locator_type}")
                else:
                    self.log.error(f"Element not displayed with locator: {locator} and locatorType: {locator_type}")
                return is_displayed
        except:
            self.log.error(f"Element not found with locator: {locator} and locatorType: {locator_type}")
            return False

    # Generic method to wait for the presence, visibility or clickability of an element - Used for explicit waits
    def wait_for_element(self, locator, locator_type="xpath", condition="present",timeout=10, poll_frequency=0.5, element=None):
        """
        List of conditions:
        1. present  - presence_of_element_located
        2. visible - visibility_of_element_located
        3. click - element_to_be_clickable
        """
        try:
            if locator:
                by_type = self.get_byType(locator_type)
                self.log.debug(f"Waiting {timeout} seconds for element with locator: {locator} and locatorType: {locator_type}")
                wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=
                [
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException
                ])
                if condition == "present":
                    element = wait.until(EC.presence_of_element_located((by_type, locator)))
                    self.log.info(f"Element appeared with locator: {locator} and locatorType: {locator_type}")
                elif condition == "visible":
                    element = wait.until(EC.visibility_of_element_located((by_type, locator)))
                    self.log.info(f"Element visible with locator: {locator} and locatorType: {locator_type}")
                elif condition == "click":
                    element = wait.until(EC.element_to_be_clickable((by_type, locator)))
                    self.log.info(f"Can click on element with locator: {locator} and locatorType: {locator_type}")
                else:
                    self.log.error(f"Invalid condition: {condition} - Use 'present', 'visible', or 'click'")
        except:
            self.log.error(f"Element not found with locator: {locator} and locatorType: {locator_type}")
        return element

    # Generic method to scroll
    def scroll_web(self, direction):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0,-800);")
            self.log.info(f"Page was scrolled {direction}")
        elif direction == "down":
            self.driver.execute_script("window.scrollBy(0,800);")
            self.log.info(f"Page was scrolled {direction}")

    # Generic method to scroll to a specific element
    def scroll_toElement(self, locator, locator_type="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.log.info(f"Page was scrolled to element with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(f"Could not scroll to element with locator: {locator} and locatorType: {locator_type}")

    # Generic method to switch frames
    def switch_frame(self, id="", name="", index=None):
        if id:
            self.driver.switch_to.frame(id)
            self.log.info(f"Switched to iframe with ID: {id}")
        elif name:
            self.driver.switch_to.frame(name)
            self.log.info(f"Switched to iframe with ID: {name}")
        else:
            self.driver.switch_to.frame(index)
            self.log.info(f"Switched to iframe with ID: {index}")

    # Method to go back to the main frame of the web
    def switchTo_defaultContent(self):
        self.driver.switch_to.default_content()

    # Method to change to an iframe by its index
    def switch_frame_byIndex(self, locator, locator_type="xpath"):
        result = False
        try:
            iframe_list = self.get_elementList(locator= "//iframe", locator_type="xpath")
            self.log.debug(f"Length of iframe list: {len(iframe_list)}")
            for i in range(len(iframe_list)):
                self.switch_frame(index=iframe_list[i])
                result = self.isElement_present(locator, locator_type)
                if result:
                    self.log.info(f"Switched to iFrame with index: {i}")
                    break
                self.switchTo_defaultContent()
            return result
        except:
            self.log.error(f"iFrame index was not found")
            return result

    # Generic method to obtain the value of a specific attribute from an element in the web
    def getElement_attributeValue(self, attribute, locator, locator_type="xpath", element=None):
        value = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            value = element.get_attribute(attribute)
            self.log.debug(f"Got the value for the attribute: {attribute}  of the element with locator: {locator}"
                  f" and locatorType: {locator_type}")
        except:
            self.log.error(f"Could not get the value for the attribute: {attribute}  of the element with locator: {locator}"
                  f" and locatorType: {locator_type}")
        return value

    def is_enabled(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        enabled = False
        try:
            attribute_value = self.getElement_attributeValue(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElement_attributeValue(element=element, attribute="class")
                self.log.info(f"Attribute value from application Web UI -> {value}")
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info(f"Enabled element with locator: {locator} and locatorType: {locator_type}")
            else:
                self.log.info(f"Disabled element with locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.error(f"State not found for element with locator: {locator} and locatorType: {locator_type}")
        return enabled

    # Generic method to take screenshots
    def screenShot(self, result_message):
        filename = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_filename = screenshot_directory + filename
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info(f"Screenshot saved to directory: {destination_file}")
        except:
            self.log.error(f"Could not take screenshot")

    # Generic method to select items in a dropdown
    def select_dropdown(self, what_to_select, locator, locator_type="xpath", select_type="value", element=None):
        """
        List of select_type:
        1. value
        2. index
        3. text
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                selection = Select(element)
                if select_type == "value":
                    selection.select_by_value(what_to_select)
                    self.log.debug(f"Element with locator: {locator} and locatorType: {locator_type} was selected with the "
                                   f"{select_type} {what_to_select}")
                    self.log.info(f"{what_to_select} was selected")
                elif select_type == "index":
                    selection.select_by_index(what_to_select)
                    self.log.debug(f"Element with locator: {locator} and locatorType: {locator_type} was selected with the "
                                   f"{select_type} {what_to_select}")
                    self.log.info(f"{what_to_select} was selected")
                elif select_type == "text":
                    selection.select_by_visible_text(what_to_select)
                    self.log.debug(f"Element with locator: {locator} and locatorType: {locator_type} was selected with the "
                                   f"{select_type} {what_to_select}")
                    self.log.info(f"{what_to_select} was selected")
                else:
                    self.log.error(f"Invalid select_type: {select_type} - Use 'value', 'index', or 'text'")
        except:
            self.log.error(f"Element not found with locator: {locator} and locatorType: {locator_type}")
        return element
