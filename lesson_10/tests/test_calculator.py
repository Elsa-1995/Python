import allure
import pytest
from selenium import webdriver
from ..pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Calculator Tests")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест калькулятора с задержкой 45 секунд")
@allure.description("Тест калькулятора с задержкой 45 секунд")
def test_slow_calculator(driver):
    calc = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc.open()

    with allure.step("Установить задержку 45 секунд"):
        calc.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        calc.calculate_7_plus_8()

    with allure.step("Дождаться результата 15 (ожидание до 50 секунд)"):
        # Используем новый метод который ждет именно результат 15
        result = calc.wait_for_result_15(timeout=50)

        # Прикрепляем отладочную информацию
        allure.attach(f"Полученный результат: '{result}'",
                      name="Result info",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверить результат"):
        assert result == "15", f"Ожидалось '15', получено '{result}'"