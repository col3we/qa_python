from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )

    input_field.send_keys("12345")
    time.sleep(1)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("54321")
    time.sleep(1)

finally:
    driver.quit()
