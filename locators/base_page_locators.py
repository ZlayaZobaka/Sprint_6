from selenium.webdriver.common.by import By


class BasePageLocators:
    # Локатор на логотип Яндекса
    yandex_link = [By.XPATH, './/a[@href = "//yandex.ru"]']

    # Локатор на логотип «Самоката»
    main_page_link = [By.XPATH, './/a[@href = "/"]']
