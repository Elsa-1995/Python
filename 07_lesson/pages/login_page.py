from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Поля для ввода
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def enter_username(self, username):
        # Находим поле и вводим логин
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        # Находим поле и вводим пароль
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        # Нажимаем кнопку входа
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        # Весь процесс входа
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()