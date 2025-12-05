from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.clear_button = (By.XPATH, "//span[text()='C']")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_button(self, button_text):
        xpath = f'//span[text()="{button_text}"]'
        self.driver.find_element(By.XPATH, xpath).click()

    def clear(self):
        try:
            self.driver.find_element(*self.clear_button).click()
        except:
            pass

    def click_buttons(self, *buttons):
        for button in buttons:
            self.click_button(button)

    def calculate_7_plus_8(self):
        self.clear()
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    def get_result(self):
        """Возвращает результат с экрана после ожидания"""
        # Ждем пока результат появится (не пустая строка)
        self.wait.until(
            lambda driver: driver.find_element(*self.screen).text.strip() != ""
        )
        # Возвращаем текст результата
        return self.driver.find_element(*self.screen).text



