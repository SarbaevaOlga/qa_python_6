import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Users
from urls import Urls


@allure.feature('Страница заказа')
class TestOrderPage:
    @allure.title('Заказ через кнопку "Заказать" - {button_type}')
    @allure.description('Позитивный тест заказа через разные кнопки')
    @pytest.mark.parametrize('user_data', [
        Users.user_1,
        Users.user_2
    ], ids=["Набор 1", "Набор 2"])
    @pytest.mark.parametrize('button_type', [
        'header',
        'footer'
    ], ids=["Верхняя кнопка", "Нижняя кнопка"])
    def test_order_via_different_buttons(self, driver, user_data, button_type):
        with allure.step('Инициализация страниц'):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            urls = Urls()

        with allure.step('Принимаем куки'):
            main_page.accept_cookies()

        with allure.step(f'Кликаем на {button_type} кнопку "Заказать"'):
            main_page.click_order_button(button_type)

        with allure.step('Заполняем первую форму заказа'):
            order_page.fill_first_order_form(user_data)
            order_page.click_next_button()

        with allure.step('Заполняем вторую форму заказа'):
            order_page.fill_second_order_form(user_data)
            order_page.click_order_button()

        with allure.step('Подтверждаем заказ'):
            order_page.confirm_order()

        with allure.step('Проверяем успешное оформление'):
            success_displayed = order_page.check_success_message()
            assert success_displayed, "Сообщение об успешном заказе должно отображаться"

            # Дополнительная проверка - что мы остались на странице заказа
            current_url = order_page.get_current_url()
            assert urls.ORDER_PAGE in current_url or "order" in current_url, "Должны остаться на странице заказа"