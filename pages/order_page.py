from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderPage:
    # Имя клиента
    name_input = [By.XPATH, './/input[@placeholder = "* Имя"]']

    # Фамилия клиента
    family_input = [By.XPATH, './/input[@placeholder = "* Фамилия"]']

    # Адрес клиента
    address_input = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']

    # Станция метро
    metro_input = [By.XPATH, './/input[@placeholder = "* Станция метро"]']

    # Телефон клиента
    phone_input = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']

    # Кнопка Далее
    next_button = [By.XPATH, './/button[text()="Далее"]']

    # Поле даты
    date_input = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']

    # Срок аренды
    lease_input = [By.XPATH, './/div[@class = "Dropdown-placeholder"]']

    # Кнопка Заказать
    make_order_btn = [By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM")][text()="Заказать"]']

    # Кнопка Да
    yes_bnt = [By.XPATH, './/button[text()="Да"]']

    # Кнопка Посмотреть статус
    view_status_btn = [By.XPATH, './/button[text() = "Посмотреть статус"]']

    # Поле Комментарий для курьера
    comment_input = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']

    @staticmethod
    def metro_stations_list_element(text):
        """
        Элемент списка станций

        :param text: название станции

        :return: локатор на указанную станцию
        """

        return [By.XPATH, f'.//div[@class = "select-search__select"]//div[text()="{text}"]']

    @staticmethod
    def lease_period_list_element(text):
        """
        Элемент списка длительностей аренды

        :param text: текст пункта, который надо выбрать

        :return: локатор на указанный пункт
        """

        return [By.XPATH, f'.//div[@class="Dropdown-menu"]/div[text()="{text}"]']

    @staticmethod
    def color_checkbox(text):
        """
        Чекбокс с нужным цветом

        :param text: текст чекбокса, который надо выбрать

        :return: локатор на указанный чекбокс
        """
        return [By.XPATH, f'.//label[text()="{text}"]']

    def __init__(self, driver):
        self.driver = driver

    def set_client_name(self, text):
        """
        Заполняем поле Имя клиента

        :param text: имя клиента
        """

        self.driver.find_element(*self.name_input).send_keys(text)

    def set_client_family(self, text):
        """
        Заполняем поле Фамилия клиента

        :param text: фамилия клиента
        """

        self.driver.find_element(*self.family_input).send_keys(text)

    def set_client_address(self, text):
        """
        Заполняем поле Адрес клиента

        :param text: адрес клиента
        """

        self.driver.find_element(*self.address_input).send_keys(text)

    def set_client_phone(self, text):
        """
        Заполняем поле Телефон

        :param text: телефон клиента
        """

        self.driver.find_element(*self.phone_input).send_keys(text)

    def select_metro_station(self, text):
        """
        Выбирает станцию метро

        :param text: название станции метро
        """

        self.driver.find_element(*self.metro_input).click()
        self.driver.find_element(*self.metro_stations_list_element(text)).click()

    def click_next_button(self):
        """
        Нажимает кнопку Далее
        """

        self.driver.find_element(*self.next_button).click()

    def set_start_date(self, text):
        """
        Заполняем поле Когда привезти самокат

        :param text: дата
        """

        element = self.driver.find_element(*self.date_input)
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    def set_lease_period(self, text):
        """
        Заполняем поле Длительность аренды

        :param text: текст пункта, который надо выбрать
        """

        self.driver.find_element(*self.lease_input).click()
        self.driver.find_element(*self.lease_period_list_element(text)).click()

    def set_color(self, text):
        """
        Заполняем поле Цвет самоката

        :param text: цвет самоката
        """

        self.driver.find_element(*self.color_checkbox(text)).click()

    def set_comment(self, text):
        """
        Заполняем поле Комментарий

        :param text: текст комментария
        """

        self.driver.find_element(*self.comment_input).send_keys(text)

    def click_make_order_button(self):
        """
        Кликает по кнопке Заказать
        """

        self.driver.find_element(*self.make_order_btn).click()

    def click_yes_button(self):
        """
        Кликает по кнопке Да
        """

        self.driver.find_element(*self.yes_bnt).click()

    def click_view_status(self):
        """
        Кликает по кнопке Посмотреть статус
        """
        self.driver.find_element(*self.view_status_btn).click()

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
