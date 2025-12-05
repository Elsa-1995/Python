from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self, delay_value):
        text_input = self.driver.find_element(*self.delay_input)
        text_input.clear()
        text_input.send_keys(delay_value)

    def click_button(self, button_text):
        xpath = f'//span[text()="{button_text}"]'
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def calculate_7_plus_8(self):
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    def get_result(self):
            self.wait.until(
                EC.text_to_be_present_in_element(self.screen, "15")
            )
            return



