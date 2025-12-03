from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    # Кнопки добавления в корзину
    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Иконка корзины
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        # Добавляем три товара в корзину
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_tshirt).click()
        self.driver.find_element(*self.add_onesie).click()

    def go_to_cart(self):
        # Переходим в корзину
        self.driver.find_element(*self.cart_icon).click()