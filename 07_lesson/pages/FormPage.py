from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы полей формы
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")

        # Локаторы для проверок
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        self.error_icon = (By.CSS_SELECTOR, ".error_icon")
        self.success_indicator = (By.CLASS_NAME, "success-message")

    def fill_form(self, first_name, last_name, zip_code):
        """Заполняет форму данными"""
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def clear_form(self):
        """Очищает форму"""
        self.driver.find_element(*self.first_name).clear()
        self.driver.find_element(*self.last_name).clear()
        self.driver.find_element(*self.zip_code).clear()

    def has_error(self):
        """Проверяет, есть ли ошибка на странице"""
        try:
            return self.driver.find_element(*self.error_message).is_displayed()
        except:
            return False

    def get_error_text(self):
        """Возвращает текст ошибки, если она есть"""
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return ""

    def are_fields_valid(self):
        """Проверяет, все ли поля валидны (нет красной обводки)"""
        try:
            # Проверяем наличие класса ошибки у полей
            fields = [
                self.driver.find_element(*self.first_name),
                self.driver.find_element(*self.last_name),
                self.driver.find_element(*self.zip_code)
            ]

            # Если у поля есть класс ошибки - оно невалидно
            for field in fields:
                if "error" in field.get_attribute("class"):
                    return False
            return True
        except:
            return False
