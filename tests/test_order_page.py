import allure
import pytest
import data.urls as urls
import data.users as users
from pages.main_page import MainPage


class TestOrderPage:

    @allure.title('Проверка флоу позитивного сценария заказа самоката.')
    @allure.description('Проверяем заказ кнопкой "Заказать" (верхнюю/нижнюю) и переходы на главную страницу/Дзен')
    @pytest.mark.parametrize(
        "user, click_order_button_func",
        [
            [users.user1, MainPage.click_header_order_button],
            [users.user2, MainPage.click_footer_order_button]
        ]
    )
    def test_positive_order_scenario(self, user, click_order_button_func, driver):
        main_page = MainPage(driver)

        main_page.click_cookie_confirm_button()
        order_page = click_order_button_func(main_page)
        order_page.make_order(user)
        order_page.click_go_to_main_page_link()
        order_page.click_go_to_yandex_link()
        order_page.switch_to_new_window(urls.DZEN_URL)

        with allure.step('Проверяем, что открылась главная страница Дзена'):
            assert driver.current_url == urls.DZEN_URL
