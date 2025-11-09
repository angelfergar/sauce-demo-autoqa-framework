import logging
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver

class StatusReporter(SeleniumDriver):
    log = cl.custom_logger(log_level=logging.INFO)

    def __init__(self, driver):
        super(StatusReporter, self).__init__(driver)
        # Create a list that will contain the result for the tests
        self.result_list = []

    # Method to add the result of each test case to the result list
    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(f"### VERIFICATION SUCCESSFUL: {result_message}")
                    self.screenShot(result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error(f"### VERIFICATION FAILED: {result_message}")
            else:
                self.log.error({f"### PAGE ERROR NONE {self.driver.title}"})
                self.result_list.append("FAIL")
                self.log.error(f"### VERIFICATION FAILED: {result_message}")
        except:
            self.result_list.append("FAIL")
            self.log.error(f"### EXCEPTION RAISED: {result_message}")

    # Method used to check the result of each test case
    def mark(self, result, result_message):
        self.set_result(result, result_message)

    # Method used at the end of each test case to check the result of the steps involved in the case
    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(f"### TEST FAILED: {test_name}")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(f"### TEST SUCCESSFUL: {test_name}")
            self.result_list.clear()
            assert True == True