from selenium.webdriver.common.by import By


class OrderPageLocators:
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
