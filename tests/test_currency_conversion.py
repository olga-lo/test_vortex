from playwright.sync_api import sync_playwright


def test_currency_conversion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Зайти на страницу
        page.goto("https://finance.rambler.ru/calculators/converter/")

        # 2. Найти инпут ввод и ввести значение 10
        amount_input = page.locator('[aria-label="Cумма"]')
        amount_input.fill("10")

        # 3. Найти селектор валюты исходной и выбрать EUR
        converter_first_select = page.locator('[data-finance_media-desktop="converter_first_select"]')
        converter_first_select.click()

        first_currency = page.locator('[data-finance_media-desktop="EUR"]').first
        first_currency.click()

        # 4
        converter_second_select = page.locator('[data-finance_media-desktop="converter_second_select"]')
        converter_second_select.click()

        second_currency = page.locator('[data-finance_media-desktop="AUD"]').nth(1)
        second_currency.click()


        # 5. Найти кнопку кнопку конвертации и кликнуть
        button_converter = page.locator('[data-finance_media-desktop="convert_link"]')
        button_converter.click()

        # # 6. Найти значение сконвертированного курса и вывести его значение
        # result = page.locator('.converter-display__value')


        value_of_converted_rate = page.locator('[class="uKWNQ"]')


        print(f"Сконвертированный курс: {value_of_converted_rate.inner_text()}")
        #
        # browser.close()
        input("Press Enter to close the browser...")


if __name__ == "__main__":
    test_currency_conversion()
