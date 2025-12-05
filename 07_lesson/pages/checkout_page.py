from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

    def has_error(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").is_displayed()
        except:
            return False

    def get_error_text(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        except:
            return ""