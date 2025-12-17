import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """Инициализация страницы калькулятора."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.clear_button = (By.XPATH, "//span[text()='C']")

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку {delay_value} секунд")
    def set_delay(self, delay_value):
        """Устанавливает значение задержки."""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text):
        """Нажимает кнопку калькулятора."""
        xpath = f'//span[text()="{button_text}"]'
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Очистить калькулятор")
    def clear(self):
        """Очищает экран калькулятора."""
        try:
            self.driver.find_element(*self.clear_button).click()
        except:
            pass

    @allure.step("Выполнить вычисление 7 + 8")
    def calculate_7_plus_8(self):
        """Выполняет операцию сложения 7 + 8."""
        self.clear()
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    @allure.step("Получить результат вычисления")
    def get_result(self):
        """Получает результат вычисления."""
        # Ожидаем пока результат изменится (не будет "7+8")
        self.wait.until(
            lambda driver: driver.find_element(*self.screen).text != "7+8"
        )
        return self.driver.find_element(*self.screen).text

    @allure.step("Дождаться результата 15")
    def wait_for_result(self, expected_result="15", timeout=50):
        """Ожидает конкретный результат."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_result)
        )
        return self.driver.find_element(*self.screen).text