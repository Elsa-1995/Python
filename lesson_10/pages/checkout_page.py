import allure
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        """Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver

    @allure.step("Заполнить форму: Имя='{first_name}', Фамилия='{last_name}', Индекс='{zip_code}'")
    def fill_form(self, first_name, last_name, zip_code):
        """Заполняет форму оформления заказа.

        Args:
            first_name (str): Имя покупателя
            last_name (str): Фамилия покупателя
            zip_code (str): Почтовый индекс

        Returns:
            None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self):
        """Нажимает кнопку Continue.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму")
    def get_total_price(self):
        """Получает итоговую сумму заказа.

        Returns:
            str: Итоговая сумма
        """
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

    @allure.step("Проверить наличие ошибки")
    def has_error(self):
        """Проверяет наличие ошибки.

        Returns:
            bool: True если есть ошибка, иначе False
        """
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").is_displayed()
        except:
            return False

    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        """Получает текст ошибки.

        Returns:
            str: Текст ошибки или пустая строка
        """
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        except:
            return ""