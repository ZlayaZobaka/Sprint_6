import allure
import pytest
import data.urls as urls
import data.users as users
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка флоу позитивного сценария заказа самоката.')
    @allure.description('Проверяем заказ кнопкой "Заказать" (верхнюю/нижнюю) и переходы на главную страницу/Дзен')
    @pytest.mark.parametrize(
        "user, button",
        [
            [users.user1, 'in_header'],
            [users.user2, 'in_footer']
        ]
    )
    def test_positive_order_scenario(self, user, button, driver):
        main_page = MainPage(driver)

        with allure.step('Закрываем панель с предупреждением об использовании cookies'):
            main_page.click_cookie_confirm_button()

        with allure.step(f'Кликаем по кнопке Заказать. Местоположение кнопки - {button}'):
            main_page.click_order_button(button)

        order_page = OrderPage(driver)

        with allure.step(f'Заполняем поля заказа, оформляем его для пользователя {user.name} {user.family}'):
            order_page.make_order(user)

        base_page = BasePage(driver)

        with allure.step('Кликаем на логотип «Самоката», переходим на главную страницу «Самоката»'):
            base_page.click_go_to_main_page_link()

        with allure.step('Кликаем на логотип Яндекса'):
            base_page.click_go_to_yandex_link()

        with allure.step('Переключаемся в новое окно, ждем конца загрузки'):
            base_page.switch_to_new_window(urls.DZEN_URL)

        with allure.step('Проверяем, что открылась главная страница Дзена'):
            assert driver.current_url == urls.DZEN_URL
