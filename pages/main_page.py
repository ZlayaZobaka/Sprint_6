from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:
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

    def __init__(self, driver):
        self.driver = driver

    def click_accordion_item_heading(self, item_number):
        """
        Cкролирует к заголовку с вопросом и клик по нему.

        :param item_number: Номер заголовка
        """

        element = self.driver.find_element(*self.item_heading_text(item_number))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.item_heading_text(item_number)))

        self.driver.find_element(*self.item_heading_text(item_number)).click()

    def accordion_item_texts(self, item_number):
        """
        Возвращает тексты вопроса и соответствующего ему ответа

        :param item_number: Номер вопроса

        :return: Кортеж с текстами вопроса и ответа
        """

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.item_panel_text(item_number)))

        return (self.driver.find_element(*self.item_heading_text(item_number)).text,
                self.driver.find_element(*self.item_panel_text(item_number)).text)

    def click_cookie_confirm_button(self):
        """
        Кликает по кнопке согласия с куками, если таковая найдена
        """

        elements = self.driver.find_elements(*self.cookie_confirm_button)
        if len(elements) > 0:
            self.driver.find_element(*self.cookie_confirm_button).click()

    def click_order_button(self, button):
        """
        Кликает по кнопке Заказать

        :param button:  Строка указывающая где искать кнопку
         возможные вариатны: 'in_header' - в шапке или 'in_footer' - в подвале
        """

        if button == 'in_header':
            self.click_header_order_button()
        elif button == 'in_footer':
            self.click_footer_order_button()
        else:
            raise TypeError('неизвестное значение')

    def click_header_order_button(self):
        """
        Кликает по кнопке Заказать в шапке
        """

        self.driver.find_element(*self.header_order_btn).click()

    def click_footer_order_button(self):
        """
        Кликает по кнопке Заказать в подвале
        """

        self.driver.find_element(*self.footer_order_btn).click()
