import allure
import pytest
from selenium import webdriver
from ..pages.login_page import LoginPage
from ..pages.products_page import ProductsPage
from ..pages.cart_page import CartPage
from ..pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.feature("SauceDemo Shop")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный цикл покупки в магазине")
@allure.description("Тест полного цикла покупки в интернет-магазине")
def test_complete_purchase_flow(driver):
    with allure.step("Открыть сайт SauceDemo"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизоваться"):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        products_page = ProductsPage(driver)
        products_page.add_backpack_to_cart()
        products_page.add_tshirt_to_cart()
        products_page.add_onesie_to_cart()

    with allure.step("Перейти в корзину"):
        products_page.go_to_cart()

    with allure.step("Проверить корзину"):
        cart_page = CartPage(driver)
        item_count = cart_page.get_item_count()

        with allure.step(f"Проверить что в корзине {item_count} товаров"):
            assert item_count == 3, f"Ожидалось 3 товара, получено {item_count}"
            print(f"✓ В корзине {item_count} товара")

    with allure.step("Оформить заказ"):
        cart_page.click_checkout()

    with allure.step("Заполнить форму оформления"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Эльза", "Воронова", "123456")
        checkout_page.click_continue()

    with allure.step("Проверить итоговую стоимость"):
        actual_price = checkout_page.get_total_price()

        with allure.step(f"Сравнить цену: получено '{actual_price}'"):
            assert "58.29" in actual_price, f"Ожидалась сумма 58.29, получено: {actual_price}"
            print(f"✓ Тест пройден! Итоговая сумма: {actual_price}")