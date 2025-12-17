import allure
from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        """Инициализация страницы товаров.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self):
        """Добавляет рюкзак в корзину.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    @allure.step("Добавить футболку в корзину")
    def add_tshirt_to_cart(self):
        """Добавляет футболку в корзину.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("Добавить комбинезон в корзину")
    def add_onesie_to_cart(self):
        """Добавляет комбинезон в корзину.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self):
        """Получает количество товаров в корзине.

        Returns:
            int: Количество товаров (0 если нет бейджа)
        """
        try:
            return int(self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
        except:
            return 0

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Переходит на страницу корзины.

        Returns:
            None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()