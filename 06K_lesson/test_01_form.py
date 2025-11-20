import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r"C:\EDGE\edgedriver_win64\msedgedriver.exe"

def test_form_validation():
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        WebDriverWait(driver, 10)

        driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
        driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()
        driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Проверка, что поле Zip code подсвечено красным
        zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").value_of_css_property("background-color")

        assert zip_code == "#f8d7da"
        fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job", "company"]

        for field in fields:
            field = driver.find_element(By.CSS_SELECTOR, "form-label").value_of_css_property("background-color")
        assert field == "#d1e7dd"

    finally:
        driver.quit()
