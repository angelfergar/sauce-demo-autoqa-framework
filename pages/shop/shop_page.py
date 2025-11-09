import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from utilities.util import Util

class ShopPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)
    utils = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _item_list = "inventory_item" # class
    _item_desc = "inventory_item_desc" # class
    _item_title = "inventory_item_name" # class
    _item_price = "inventory_item_price" # class
    _first_item ="(//div[@class='inventory_item_description'])[1]//div[@class='inventory_item_name ']"
    _add_button = "btn.btn_primary.btn_small.btn_inventory" # class
    _remove_button = "btn.btn_secondary.btn_small.btn_inventory" # class
    _filter = "product_sort_container" # class
    _shopping_quantity = "shopping_cart_badge" # class
    _shopping_cart = "shopping_cart_link" # class

    # Expected info
    inventory_data = utils.get_data("inventory_data.csv")
    expected_titles = [column[0] for column in inventory_data]
    expected_descs = [column[1] for column in inventory_data]
    expected_prices = [column[2] for column in inventory_data]

    # Methods to perform actions on the web
    def click_add_item(self):
        add_buttons = self.get_elementList(locator=self._add_button, locator_type="class")
        for button in add_buttons:
            self.element_click(element=button)

    def add_one_item(self):
        self.wait_for_element(self._filter, locator_type="class")
        add_buttons = self.get_elementList(locator=self._add_button, locator_type="class")
        self.element_click(element=add_buttons[0])

    def get_item_text(self):
        return self.get_text(self._first_item)

    def click_cart_button(self):
        self.element_click(self._shopping_cart, locator_type="class")

    def click_remove_button(self):
        remove_buttons = self.get_elementList(locator=self._remove_button, locator_type="class")
        for button in remove_buttons:
            self.element_click(element=button)

    def titles_asc(self):
        items_text = self.get_elementsText(locator=self._item_title, locator_type="class")
        sorted_text = sorted(items_text, reverse=True)
        return sorted_text
    def titles_desc(self):
        items_text = self.get_elementsText(locator=self._item_title, locator_type="class")
        sorted_text = sorted(items_text)
        return sorted_text

    def prices_asc(self):
        items_text = self.get_elementsText(locator=self._item_price, locator_type="class")
        clean_prices = [price.replace('$', '').strip() for price in items_text]
        sorted_prices = sorted(clean_prices, key=float)
        sorted_prices_check = [f"${price}" for price in sorted_prices]
        return sorted_prices_check

    def prices_desc(self):
        items_text = self.get_elementsText(locator=self._item_price, locator_type="class")
        clean_prices = [price.replace('$', '').strip() for price in items_text]
        sorted_prices = sorted(clean_prices, key=float, reverse=True)
        sorted_prices_check = [f"${price}" for price in sorted_prices]
        return sorted_prices_check
    def sort_title_asc(self):
        self.select_dropdown("za",locator=self._filter, locator_type="class")

    def sort_price_asc(self):
        self.select_dropdown("lohi",locator=self._filter, locator_type="class")

    def sort_price_desc(self):
        self.select_dropdown("hilo", locator=self._filter, locator_type="class")

    # Methods to verify the information of the inventory
    def verify_list_length(self):
        self.wait_for_element(self._filter, locator_type="class")
        _list = self.get_elementList(self._item_list, locator_type="class")
        result = self.utils.verify_list_length(self.expected_titles, _list)
        return result

    def verify_list_titles(self):
        items_text = self.get_elementsText(locator=self._item_title, locator_type="class")
        results = []
        for item_text in items_text:
            result = self.util.verify_text_contains(item_text,str(self.expected_titles))
            results.append(result)
        return all(results)

    def verify_title_order(self, sorting="desc"):
        items_text = self.get_elementsText(locator=self._item_title, locator_type="class")
        sorted_titles = ""
        if sorting == "desc":
            sorted_titles = self.titles_desc()
        if sorting == "asc":
            sorted_titles = self.titles_asc()
        result = self.util.verify_text_match(str(items_text), str(sorted_titles))
        return result
    def verify_list_descs(self):
        items_text = self.get_elementsText(locator=self._item_desc, locator_type="class")
        results = []
        for item_text in items_text:
            result = self.util.verify_text_contains(item_text,str(self.expected_descs))
            results.append(result)
        return all(results)

    def verify_list_prices(self):
        items_text = self.get_elementsText(locator=self._item_price, locator_type="class")
        results = []
        for item_text in items_text:
            result = self.util.verify_text_contains(item_text, str(self.expected_prices))
            results.append(result)
        return all(results)

    def verify_price_order(self, sorting="asc"):
        items_text = self.get_elementsText(locator=self._item_price, locator_type="class")
        sorted_prices = ""
        if sorting == "asc":
            sorted_prices = self.prices_asc()
        elif sorting == "desc":
            sorted_prices = self.prices_desc()
        else:
            self.log.error(f"Invalid sorting method. Please select 'asc' or 'desc'")
        result = self.util.verify_text_match(str(items_text), str(sorted_prices))
        return result

    def verify_add_button(self):
        items_list = self.get_elementList(locator=self._item_list, locator_type="class")
        results = []
        for item in items_list:
            button = self.get_element_child(item, locator=self._add_button, locator_type="class")
            result = self.isElement_present(element=button)
            results.append(result)
        return all(results)

    def verify_remove_button(self):
        items_list = self.get_elementList(locator=self._item_list, locator_type="class")
        results = []
        for item in items_list:
            button = self.get_element_child(item, locator=self._remove_button, locator_type="class")
            result = self.isElement_present(element=button)
            results.append(result)
        return all(results)

    def verify_added_items(self, quantity):
        self.wait_for_element(locator=self._shopping_quantity, locator_type="class")
        quantity_text = self.get_text(locator=self._shopping_quantity, locator_type="class")
        result = self.utils.verify_text_match(quantity_text, str(quantity))
        return result

    def verify_removed_items(self):
        result = self.isElement_displayed(locator=self._shopping_quantity, locator_type="class")
        return not result










