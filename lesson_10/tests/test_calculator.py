import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

    with allure.step("Дождаться результата (без sleep)"):
        # Используем WebDriverWait для ожидания результата
        wait = WebDriverWait(driver, 50)  # 50 секунд максимум

        # Ждем пока результат не станет "15"
        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                "15"
            )
        )

        # Получаем текст результата
        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text

    with allure.step("Проверить результат"):
        assert result_text == "15", f"Ожидалось '15', получено '{result_text}'"