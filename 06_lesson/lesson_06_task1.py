from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()

    wait = WebDriverWait(driver, 20)
    green_banner = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    print(green_banner.text)

finally:
    driver.quit()