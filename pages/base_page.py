from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.base_page import BasePageLocators as Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_go_to_yandex_link(self):
        """
        Кликает по логотипу Яндекса
        """

        self.driver.find_element(*Locators.yandex_link).click()

    def click_go_to_main_page_link(self):
        """
        Кликает на логотип «Самоката»
        """

        self.driver.find_element(*Locators.main_page_link).click()

    def switch_to_new_window(self, url):
        """
        Обрабатывает появление нового окна. Ждет появления окна и конца загрузки страницы

        :param url: url ожидаемой страницы в новом окне
        """

        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url == url
        )
