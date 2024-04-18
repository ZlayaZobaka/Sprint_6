from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.main_page import MainPageLocators as Locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_accordion_item_heading(self, item_number):
        """
        Cкролирует к заголовку с вопросом и клик по нему.

        :param item_number: Номер заголовка
        """

        element = self.driver.find_element(*Locators.item_heading_text(item_number))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.item_heading_text(item_number)))

        self.driver.find_element(*Locators.item_heading_text(item_number)).click()

    def accordion_item_texts(self, item_number):
        """
        Возвращает тексты вопроса и соответствующего ему ответа

        :param item_number: Номер вопроса

        :return: Кортеж с текстами вопроса и ответа
        """

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.item_panel_text(item_number)))

        return (self.driver.find_element(*Locators.item_heading_text(item_number)).text,
                self.driver.find_element(*Locators.item_panel_text(item_number)).text)

    def click_cookie_confirm_button(self):
        """
        Кликает по кнопке согласия с куками, если таковая найдена
        """

        elements = self.driver.find_elements(*Locators.cookie_confirm_button)
        if len(elements) > 0:
            self.driver.find_element(*Locators.cookie_confirm_button).click()

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

        self.driver.find_element(*Locators.header_order_btn).click()

    def click_footer_order_button(self):
        """
        Кликает по кнопке Заказать в подвале
        """

        self.driver.find_element(*Locators.footer_order_btn).click()
