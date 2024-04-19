import allure
from locators.main_page_locators import MainPageLocators as Locators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_accordion_item_heading(self, item_number):
        """
        Cкролирует к заголовку с вопросом и клик по нему.

        :param item_number: Номер заголовка
        """

        with allure.step(f'Cкролируем к {item_number + 1}-му заголовку с вопросом и кликаем по нему'):
            self.scroll_to_element(Locators.item_heading_text(item_number))
            self.find_element(Locators.item_heading_text(item_number)).click()

    def accordion_item_texts(self, item_number):
        """
        Возвращает тексты вопроса и соответствующего ему ответа

        :param item_number: Номер вопроса

        :return: Кортеж с текстами вопроса и ответа
        """

        with allure.step(f'Получаем тексты {item_number + 1}-го вопроса и ответа'):
            return (self.find_element(Locators.item_heading_text(item_number)).text,
                    self.find_element(Locators.item_panel_text(item_number)).text)

    def click_cookie_confirm_button(self):
        """
        Кликает по кнопке согласия с куками
        """
        with allure.step('Закрываем панель с предупреждением об использовании cookies'):
            self.find_element(Locators.cookie_confirm_button).click()

    def click_header_order_button(self):
        """
        Кликает по кнопке Заказать в шапке
        """

        with allure.step(f'Кликаем по кнопке Заказать в заголовке'):
            self.find_element(Locators.header_order_btn).click()

        return OrderPage(self.driver)

    def click_footer_order_button(self):
        """
        Кликает по кнопке Заказать в подвале
        """

        with allure.step(f'Кликаем по кнопке Заказать в подвале'):
            self.find_element(Locators.footer_order_btn).click()

        return OrderPage(self.driver)
