from selenium.webdriver.common.keys import Keys
from locators.order_page import OrderPageLocators as Locators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def set_client_name(self, text):
        """
        Заполняем поле Имя клиента

        :param text: имя клиента
        """

        self.driver.find_element(*Locators.name_input).send_keys(text)

    def set_client_family(self, text):
        """
        Заполняем поле Фамилия клиента

        :param text: фамилия клиента
        """

        self.driver.find_element(*Locators.family_input).send_keys(text)

    def set_client_address(self, text):
        """
        Заполняем поле Адрес клиента

        :param text: адрес клиента
        """

        self.driver.find_element(*Locators.address_input).send_keys(text)

    def set_client_phone(self, text):
        """
        Заполняем поле Телефон

        :param text: телефон клиента
        """

        self.driver.find_element(*Locators.phone_input).send_keys(text)

    def select_metro_station(self, text):
        """
        Выбирает станцию метро

        :param text: название станции метро
        """

        self.driver.find_element(*Locators.metro_input).click()
        self.driver.find_element(*Locators.metro_stations_list_element(text)).click()

    def click_next_button(self):
        """
        Нажимает кнопку Далее
        """

        self.driver.find_element(*Locators.next_button).click()

    def set_start_date(self, text):
        """
        Заполняем поле Когда привезти самокат

        :param text: дата
        """

        element = self.driver.find_element(*Locators.date_input)
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    def set_lease_period(self, text):
        """
        Заполняем поле Длительность аренды

        :param text: текст пункта, который надо выбрать
        """

        self.driver.find_element(*Locators.lease_input).click()
        self.driver.find_element(*Locators.lease_period_list_element(text)).click()

    def set_color(self, text):
        """
        Заполняем поле Цвет самоката

        :param text: цвет самоката
        """

        self.driver.find_element(*Locators.color_checkbox(text)).click()

    def set_comment(self, text):
        """
        Заполняем поле Комментарий

        :param text: текст комментария
        """

        self.driver.find_element(*Locators.comment_input).send_keys(text)

    def click_make_order_button(self):
        """
        Кликает по кнопке Заказать
        """

        self.driver.find_element(*Locators.make_order_btn).click()

    def click_yes_button(self):
        """
        Кликает по кнопке Да
        """

        self.driver.find_element(*Locators.yes_bnt).click()

    def click_view_status(self):
        """
        Кликает по кнопке Посмотреть статус
        """
        self.driver.find_element(*Locators.view_status_btn).click()

    def make_order(self, user):
        """
        Шаг содания нового заказа

        :param user: структура типа data.users.Users
        """

        self.set_client_name(user.name)
        self.set_client_family(user.family)
        self.set_client_address(user.address)
        self.select_metro_station(user.metro_station)
        self.set_client_phone(user.phone)

        self.click_next_button()

        self.set_start_date(user.date)
        self.set_lease_period(user.lease_period)
        self.set_color(user.color)
        self.set_comment(user.comment)

        self.click_make_order_button()
        self.click_yes_button()
        self.click_view_status()
