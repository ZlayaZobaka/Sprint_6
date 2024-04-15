from selenium.webdriver.common.by import By


class MainPage:
    # Локаторы вопросов в разделе "Вопросы о важном". х - номер вопроса
    def heading_button(self, x): return [By.ID, f"accordion__heading-{x}"]
    # Локаторы ответов в разделе "Вопросы о важном". х - номер ответа
    def panel_text(self, x): return [By.XPATH, f".//div[@id='accordion__heading-{x}']/following::div/p"]

    # Кнопка согласия использования кук
    cookie_confirm_button = [By.ID, 'rcc-confirm-button']

    # Кнопка Заказать в шапке
    header_order_btn = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']

    # Кнопка Заказать в подвале
    footer_order_btn = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']

    def __init__(self, driver):
        self.driver = driver

    # клик по заголовку с вопросом. х - номер вопроса
    def click_accordion_item_heading_button(self, item_number):
        self.driver.find_element(*self.heading_button(item_number)).click()
        a = 0

    # метод возвращает текст ответа
    def accordion_item_panel_text(self, item_number):
        return self.driver.find_element(*self.panel_text(item_number)).text

    # кликаем по кнопке согласия с куками, если найдем
    def click_cookie_confirm_button(self):
        elements = self.driver.find_elements(*self.cookie_confirm_button)
        if len(elements) > 0:
            self.driver.find_element(*self.cookie_confirm_button).click()

    # кликаем по кнопке Заказать в шапке
    def click_header_order_button(self):
        self.driver.find_element(*self.header_order_btn).click()

    # кликаем по кнопке Заказать в подвале
    def click_footer_order_button(self):
        self.driver.find_element(*self.footer_order_btn).click()