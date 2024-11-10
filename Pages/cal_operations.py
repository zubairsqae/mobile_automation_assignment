from Utility.driver_setup import AppiumDriverSingleton
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CalOperations:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CalOperations, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            "value9_xpath": '//android.widget.ImageButton[@content-desc="9"]',
            "value5_xpath": '//android.widget.ImageButton[@content-desc="5"]',
            "Addition_xpath": '//android.widget.ImageButton[@content-desc="plus"]',
            "Subtraction_xpath": '//android.widget.ImageButton[@content-desc="minus"]',
            "Multiplication_xpath": '//android.widget.ImageButton[@content-desc="multiply"]',
            "Division_xpath": '//android.widget.ImageButton[@content-desc="divide"]',
            "equals_xpath": '//android.widget.ImageButton[@content-desc="equals"]',
            "AC_xpath": '//android.widget.ImageButton[@content-desc="clear"]',
            "results_path": '//android.widget.TextView',
        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    def click_element(self, element_name):
        self.find_element(element_name).click()

    def get_result_text(self):
        return self.find_element("results_path").text

    def perform_addition(self):
        try:
            self.click_element("value9_xpath")
            self.click_element("Addition_xpath")
            self.click_element("value5_xpath")
            self.click_element("equals_xpath")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def perform_subtraction(self):
        try:
            self.click_element("value9_xpath")
            self.click_element("Subtraction_xpath")
            self.click_element("value5_xpath")
            self.click_element("equals_xpath")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def perform_multiplication(self):
        try:
            self.click_element("value9_xpath")
            self.click_element("Multiplication_xpath")
            self.click_element("value5_xpath")
            self.click_element("equals_xpath")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def perform_division(self):
        try:
            self.click_element("value9_xpath")
            self.click_element("Division_xpath")
            self.click_element("value5_xpath")
            self.click_element("equals_xpath")
        except Exception as e:
            print(f"Exception occurred: {e}")
