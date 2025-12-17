import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """Инициализация страницы авторизации.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        """Открывает указанный URL.

        Args:
            url (str): URL для открытия

        Returns:
            None
        """
        self.driver.get(url)

    @allure.step("Выполнить вход с логином '{username}'")
    def login(self, username, password):
        """Выполняет авторизацию.

        Args:
            username (str): Имя пользователя
            password (str): Пароль пользователя

        Returns:
            None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()