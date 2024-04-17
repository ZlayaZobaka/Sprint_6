import allure
import pytest
from data.texts import TEXT_ITEMS
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка текстов раздела Вопросы о важном')
    @allure.description('Проверяем утверждение "когда нажимаешь на стрелочку, открывается соответствующий текст" (с)')
    @pytest.mark.parametrize(
        "item_number", [x for x in range(0, 8)]
    )
    def test_accordion_section_compare_text_in_item(self, item_number, driver):
        main_page = MainPage(driver)

        with allure.step('Закрываем панель с предупреждением об использовании cookies'):
            main_page.click_cookie_confirm_button()

        with allure.step(f'Cкролируем к {item_number + 1}-му заголовку с вопросом и кликаем по нему'):
            main_page.click_accordion_item_heading(item_number)

        with allure.step(f'Получаем тексты {item_number + 1}-го вопроса и ответа'):
            text_item = main_page.accordion_item_texts(item_number)

        with allure.step('Сравниваем тесты с ожидаемыми'):
            assert text_item == TEXT_ITEMS[item_number]
