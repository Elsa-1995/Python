from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_shop_total():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()

    try:
        # Шаг 1: Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизация как пользователь standard_user
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Ожидание загрузки страницы с товарами
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        # Шаг 3: Добавление товаров в корзину
        # Sauce Labs Backpack
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()

        # Sauce Labs Bolt T-Shirt
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()

        # Sauce Labs Onesie
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()

        # Шаг 4: Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Ожидание загрузки страницы корзины
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )

        # Шаг 5: Нажать Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Ожидание загрузки формы checkout
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout_info_container"))
        )

        # Шаг 6: Заполнить форму данными
        first_name_field = driver.find_element(By.ID, "first-name")
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys("Эльза")
        last_name_field.send_keys("Воронова")
        postal_code_field.send_keys("123456")

        # Шаг 7: Нажать кнопку Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Ожидание загрузки страницы с итоговой стоимостью
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )

        # Шаг 8: Прочитать итоговую стоимость
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_value = total_text.split("$")[1]  # Извлекаем числовое значение

        # Шаг 9: Проверить, что итоговая сумма равна $58.29
        expected_total = "58.29"
        assert total_value == expected_total, f"Ожидаемая сумма: ${expected_total}, Фактическая: ${total_value}"

        print(f"Тест пройден! Итоговая сумма: ${total_value}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise e

    finally:
        # Закрыть браузер
        driver.quit()


if __name__ == "__main__":
    test_shop_total()
