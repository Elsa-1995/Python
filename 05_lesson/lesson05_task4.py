from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/login")

input_element = driver.find_element(By.CSS_SELECTOR, "#username")

input_element.send_keys("tomsmith")

sleep(3)

input_element = driver.find_element(By.CSS_SELECTOR, "#password")

input_element.send_keys("SuperSecretPassword!")

sleep(3)

select_blue_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
select_blue_button.click()

sleep(3)

message = driver.find_element(By.CLASS_NAME, "flash")
print(message.text)
sleep(3)

driver.quit()