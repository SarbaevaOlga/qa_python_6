import pytest
import allure
from pages.main_page import MainPage
from data import faq_data
from urls import Urls

@pytest.mark.usefixtures('driver')
@allure.feature('Главная страница')
class TestMainPage:
    @allure.title('Проверка ответов в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('index, expected_answer', [(i, data[1]) for i, data in enumerate(faq_data)])
    def test_faq_section(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(index)
        actual_answer = main_page.get_answer_text(index)
        actual_clean = ' '.join(actual_answer.split())
        expected_clean = ' '.join(expected_answer.split())
        assert actual_clean == expected_clean

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_scooter_logo()
        urls = Urls()
        current_url = main_page.get_current_url()
        assert current_url == urls.MAIN_PAGE

    @allure.title('Проверка перехода на Дзен по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        original_window = main_page.get_current_window_handle()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window(original_window, timeout=10)
        window_handles = main_page.get_window_handles()
        new_window = [window for window in window_handles if window != original_window][0]
        main_page.switch_to_window(new_window)
        main_page.wait_for_url_contains(Urls.DZEN_URL_PART, timeout=15)
        current_url = main_page.get_current_url()
        assert Urls.DZEN_URL_PART in current_url
        main_page.close_current_window()
        main_page.switch_to_window(original_window)