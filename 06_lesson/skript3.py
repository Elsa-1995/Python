from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 100)

wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))

images = driver.find_elements(By.TAG_NAME, "img")

print(len(images))

src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(src)

driver.quit()
