import pytest
import data.urls as Urls
from data.data_main_page import AccordionTexts
from pages.main_page import MainPage
from selenium import webdriver


class TestMainPage:
    driver = None

    # создание драйвера для браузера Firefox
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    # Проверяем, что когда нажимаешь на стрелочку, открывается соответствующий текст (с)
    @pytest.mark.parametrize(
        "item_number", [x for x in range(0, 8)]
    )
    def test_accordion_section_compare_text_in_item(self, item_number):
        self.driver.get(Urls.BASE_URL)

        main_page = MainPage(self.driver)
        main_page.click_cookie_confirm_button()
        main_page.click_accordion_item_heading_button(item_number)
        text = main_page.accordion_item_panel_text(item_number)

        assert text == AccordionTexts.answers[item_number], 'Текст не совпадает с ожидаемым'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
