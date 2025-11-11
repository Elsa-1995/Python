from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/inputs")

input_element = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_element.send_keys("Sky")

sleep(3)

input_element.clear()

sleep(3)

input_element.send_keys("Pro")

sleep(3)

driver.quit()


