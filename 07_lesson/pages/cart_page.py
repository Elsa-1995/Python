from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Кнопка оформления заказа
    checkout_button = (By.ID, "checkout")

    # Товары в корзине
    item_names = (By.CLASS_NAME, "inventory_item_name")

    def click_checkout(self):
        # Нажимаем кнопку Checkout
        self.driver.find_element(*self.checkout_button).click()

    def check_cart_items(self):
        # Проверяем что в корзине 3 товара
        items = self.driver.find_elements(*self.item_names)
        return len(items) == 3