from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    def get_item_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()