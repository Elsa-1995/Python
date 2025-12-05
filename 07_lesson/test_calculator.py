import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    # Только здесь драйвер закрывается, не нужно driver.quit() в тесте!
    driver.quit()


def test_slow_calculator(driver):
    """Тест калькулятора с задержкой 45 секунд"""
    calc = CalculatorPage(driver)

    # 1. Открыть страницу
    calc.open()

    # 2. Установить задержку
    calc.set_delay(45)

    # 3. Выполнить вычисление
    calc.calculate_7_plus_8()

    # 4. Получить результат
    result = calc.get_result()

    # 5. Проверить результат (assert в тесте!)
    assert result == "15", f"Ожидалось '15', получено '{result}'"