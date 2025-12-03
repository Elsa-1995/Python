import pytest
from selenium import webdriver
from pages.CalcPage import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.set_delay(45)
    calculator.calculate_7_plus_8()
    result = calculator.get_result()
    assert result == "15"

    driver.quit()