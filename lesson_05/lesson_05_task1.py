from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"))
    )
    blue_button.click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()

finally:
    driver.quit()
