from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка согласия использования кук
    cookie_confirm_button = [By.ID, 'rcc-confirm-button']

    # Кнопка Заказать в шапке
    header_order_btn = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']

    # Кнопка Заказать в подвале
    footer_order_btn = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']

    @staticmethod
    def item_heading_text(x):
        """
        Вопрос в пункте разделе "Вопросы о важном"

        :param x: номер пункта

        :return: локатор на текст вопроса
        """

        return By.XPATH, f".//div[@id = 'accordion__heading-{x}']"

    @staticmethod
    def item_panel_text(x):
        """
        Ответ в пункте разделе "Вопросы о важном"

        :param x: номер пункта

        :return: локатор на текст ответа
        """
        return By.XPATH, f".//div[@id='accordion__heading-{x}']/following::div/p"
