from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Поля формы
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    zip_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    # Итоговая стоимость
    total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, zip_code):
        # Заполняем форму
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_field).send_keys(zip_code)

    def click_continue(self):
        # Нажимаем Continue
        self.driver.find_element(*self.continue_button).click()

    def check_total_price(self):
        # Проверяем итоговую стоимость
        price_text = self.driver.find_element(*self.total_price).text
        # Извлекаем число из текста "$58.29"
        actual_price = price_text.split("$")[1]
        return actual_price