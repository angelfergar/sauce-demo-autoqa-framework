import logging
import utilities.custom_logger as cl
import time
import random, string
import traceback
import pandas as pd


class Util():

    log = cl.custom_logger(logging.INFO)

    # Generic method for waiting a specific amount of time
    def sleep(self, sec, info=""):
        if info is not None:
            self.log.debug(f"Waiting {sec} seconds for {info}")
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alphaNumeric(self, length, type="letters"):
        alpha_num = ''
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count=10):
        return self.get_alphaNumeric(char_count, 'lower')

    def get_unique_nameList(self, list_size=5, item_length=None):
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    # Generic method to verify a text contains the expected text
    def verify_text_contains(self, actual_text, expected_text):
        self.log.info(f"Actual Text from Application Web UI -> {actual_text}")
        self.log.info(f'Expected Text from Application Web UI -> {expected_text}')
        if actual_text.lower() in expected_text.lower():
            self.log.debug("Text correctly contains the expected content")
            return True
        else:
            self.log.error("Text does not contain the expected content")
            return False

    # Generic method to verify a text matches the expected text
    def verify_text_match(self, actual_text, expected_text):
        self.log.info(f"Actual Text from Application Web UI -> {actual_text}")
        self.log.info(f'Expected Text from Application Web UI -> {expected_text}')
        if actual_text.lower() == expected_text.lower():
            self.log.info("Text correctly contains the expected content")
            return True
        else:
            self.log.error("Text does not contain the expected content")
            return False

    # Generic method to verify a list contains the expected elements
    def verify_list(self, expected_list, actual_list):
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] in actual_list:
                self.log.info(f"{expected_list[i]} is on the list ")
                return True
            else:
                self.log.error(f"{expected_list[i]} is on the list ")
                return False

    # Generic method to verify a list contains a certain amount of elements
    def verify_list_length(self, expected_list, actual_list):
        expected_length = len(expected_list)
        actual_length = len(actual_list)
        if expected_length == actual_length:
            self.log.info("The list's length is the same as the expected")
            return True
        else:
            self.log.error("The list's length is not the same as the expected")
            return False

    # Generic method to get the values from a table
    def get_data(self, csv_file):
        df = pd.read_csv(csv_file, skiprows=1, header=None)
        rows = df.values.tolist()
        return rows
