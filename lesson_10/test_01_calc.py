import allure
from selenium import webdriver
from lesson_10.calculator_page import CalculatorPage

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка медленного калькулятора (7 + 8 = 15)")
@allure.description(
    "Тест проверяет сложение чисел в калькуляторе "
    "с задержкой 45 секунд"
)
def test_slow_calculator() -> None:
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        calc_page = CalculatorPage(driver)

        with allure.step(
            "Открыть страницу калькулятора и задать задержку"
        ):
            calc_page.open()
            calc_page.set_delay("45")

        with allure.step("Выполнить арифметические действия"):
            calc_page.click_button("7")
            calc_page.click_button("+")
            calc_page.click_button("8")
            calc_page.click_button("=")

        with allure.step("Дождаться результата и получить значение"):
            result = calc_page.get_result(50)

        with allure.step("Проверить, что результат равен 15"):
            assert result == "15"

    finally:
        driver.quit()
