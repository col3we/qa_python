import allure
from selenium import webdriver
from lesson_10.shop_pages import (
    LoginPage,
    ProductsPage,
    CartPage,
    CheckoutPage,
)


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка оформления заказа на SauceDemo")
@allure.description(
    "Тест авторизуется, добавляет товары, оформляет заказ "
    "и проверяет итоговую сумму"
)
def test_saucedemo_purchase() -> None:
    driver = webdriver.Firefox()
    driver.maximize_window()
    total_text = ""

    try:
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть сайт и авторизоваться"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину и перейти в нее"):
            products_page.add_item_to_cart(
                "add-to-cart-sauce-labs-backpack"
            )
            products_page.add_item_to_cart(
                "add-to-cart-sauce-labs-bolt-t-shirt"
            )
            products_page.add_item_to_cart(
                "add-to-cart-sauce-labs-onesie"
            )
            products_page.go_to_cart()

        with allure.step("Нажать Checkout"):
            cart_page.click_checkout()

        with allure.step("Заполнить форму и получить стоимость"):
            checkout_page.fill_form("Иван", "Петров", "101000")
            total_text = checkout_page.get_total_text()

    finally:
        driver.quit()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total_text == "Total: $58.29"
