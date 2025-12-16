import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """Инициализация страницы калькулятора.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.clear_button = (By.XPATH, "//span[text()='C']")

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку {delay_value} секунд")
    def set_delay(self, delay_value):
        """Устанавливает значение задержки.

        Args:
            delay_value (int): Значение задержки в секундах

        Returns:
            None
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text):
        """Нажимает кнопку калькулятора.

        Args:
            button_text (str): Текст на кнопке

        Returns:
            None
        """
        xpath = f'//span[text()="{button_text}"]'
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Очистить калькулятор")
    def clear(self):
        """Очищает экран калькулятора.

        Returns:
            None
        """
        try:
            self.driver.find_element(*self.clear_button).click()
        except:
            pass

    @allure.step("Выполнить вычисление 7 + 8")
    def calculate_7_plus_8(self):
        """Выполняет операцию сложения 7 + 8.

        Returns:
            None
        """
        self.clear()
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    @allure.step("Получить результат вычисления")
    def get_result(self):
        """Получает результат вычисления.

        Returns:
            str: Результат вычисления
        """
        # Ждем пока результат появится (не пустая строка)
        self.wait.until(
            lambda driver: driver.find_element(*self.screen).text.strip() != ""
        )
        # Возвращаем текст результата
        return self.driver.find_element(*self.screen).text

    @allure.step("Дождаться результата 15")
    def wait_for_result_15(self, timeout=50):
        """Ожидает пока результат не станет равным '15'.

        Args:
            timeout (int): Максимальное время ожидания в секундах

        Returns:
            str: Результат вычисления
        """
        # Создаем новый wait с указанным timeout
        wait = WebDriverWait(self.driver, timeout)

        # Ждем пока результат не станет '15'
        wait.until(
            lambda driver: driver.find_element(*self.screen).text.strip() == "15"
        )

        # Возвращаем результат
        return self.driver.find_element(*self.screen).text