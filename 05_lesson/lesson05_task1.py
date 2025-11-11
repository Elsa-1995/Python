from time import sleep, process_time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://uitestingplayground.com/classattr")

sleep(5)

blue_button = ".btn-primary"
select_blue_button = driver.find_element(By.CSS_SELECTOR, blue_button)

sleep(5)

select_blue_button.click()
print("Успешно кликнули на синюю кнопку")