# Pytest test class
import pytest

from Pages.cal_operations import CalOperations


@pytest.fixture(scope="class")
def calculator():
    # Initialize calculator instance for the test class
    cal_instance = CalOperations()
    yield cal_instance
    # Teardown
    cal_instance.driver.quit()


class TestCal_Opr:
    def test_addition(self, calculator):
        calculator.perform_addition()
        result = calculator.get_result_text()
        assert result == "14", f"Expected result 14, got {result}"

    def test_subtraction(self, calculator):
        calculator.perform_subtraction()
        result = calculator.get_result_text()
        assert result == "4", f"Expected result 4, got {result}"

    def test_division(self, calculator):
        calculator.perform_division()
        result = calculator.get_result_text()
        assert result == "1", f"Expected result 1.8, got {result}"

    def test_multiplication(self, calculator):
        calculator.perform_multiplication()
        result = calculator.get_result_text()
        assert result == "45", f"Expected result 45, got {result}"
