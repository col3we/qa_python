from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class ProductsPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_id: str) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable((By.ID, item_id))
        ).click()

    def go_to_cart(self) -> None:
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()


class CheckoutPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located(
                self.first_name_field
            )
        ).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(
            last_name
        )
        self.driver.find_element(*self.postal_code_field).send_keys(
            postal_code
        )
        self.driver.find_element(*self.continue_button).click()

    def get_total_text(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text
