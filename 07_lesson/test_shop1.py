from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

# Создаем драйвер
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуемся
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавляем товары в корзину
    products_page = ProductsPage(driver)
    products_page.add_items_to_cart()

    # 4. Переходим в корзину
    products_page.go_to_cart()

    # 5. Проверяем корзину и оформляем заказ
    cart_page = CartPage(driver)

    if cart_page.check_cart_items():
        print("✓ В корзине 3 товара")
    else:
        print("✗ Ошибка: не все товары в корзине")

    cart_page.click_checkout()

    # 6. Заполняем форму
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Эльза", "Воронова", "123456")
    checkout_page.click_continue()

    # 7. Проверяем итоговую стоимость
    actual_price = checkout_page.check_total_price()
    expected_price = "58.29"

    if actual_price == expected_price:
        print(f"✓ Тест пройден! Итоговая сумма: ${actual_price}")
    else:
        print(f"✗ Ошибка! Ожидалось: ${expected_price}, Получено: ${actual_price}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер
      driver.quit()