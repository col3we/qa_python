from selenium import webdriver

from shop_pages import CartPage, CheckoutPage, LoginPage, ProductsPage


def test_saucedemo_purchase():
    driver = webdriver.Firefox()
    driver.maximize_window()
    total_text = ""

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        products_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
        products_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        products_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")
        products_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Иван", "Петров", "101000")
        total_text = checkout_page.get_total_text()

    finally:
        driver.quit()

    assert total_text == "Total: $58.29"
