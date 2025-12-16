import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """Инициализация страницы корзины.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver

    @allure.step("Получить количество товаров в корзине")
    def get_item_count(self):
        """Получает количество товаров в корзине.

        Returns:
            int: Количество товаров
        """
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    @allure.step("Получить названия товаров")
    def get_item_names(self):
        """Получает названия товаров в корзине.

        Returns:
            list: Список названий товаров
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self):
        """Нажимает кнопку Checkout.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "checkout").click()