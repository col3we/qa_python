from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen_locator = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, label: str):
        xpath = f"//span[text()='{label}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, timeout: int = 50) -> str:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.screen_locator, "15")
        )
        return self.driver.find_element(*self.screen_locator).text
