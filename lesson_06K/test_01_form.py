from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form_submission():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "data-types.html"
        )

        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for field_name, value in form_data.items():
            driver.find_element(By.NAME, field_name).send_keys(value)

        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        wait = WebDriverWait(driver, 10)
        zip_code_field = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )

        assert "alert-danger" in zip_code_field.get_attribute("class")
        assert (
            zip_code_field.value_of_css_property("background-color")
            == "rgba(248, 215, 218, 1)"
        )

        for field_id in form_data.keys():
            field = driver.find_element(By.ID, field_id)
            assert (
                "alert-success" in field.get_attribute("class")
            ), f"Поле {field_id} не зеленое"
            assert (
                field.value_of_css_property("background-color")
                == "rgba(209, 231, 221, 1)"
            )

    finally:
        driver.quit()
