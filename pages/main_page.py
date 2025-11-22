import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Принять куки')
    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)
            )
            cookie_button.click()
        except:
            pass

    @allure.step('Кликнуть на вопрос с индексом {index}')
    def click_question(self, index):
        locator = (By.CSS_SELECTOR, MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step('Получить текст ответа для вопроса с индексом {index}')
    def get_answer_text(self, index):
        locator = (By.CSS_SELECTOR, MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index))
        return self.get_element_text(locator)

    @allure.step('Кликнуть на кнопку "Заказать" типа {button_type}')
    def click_order_button(self, button_type):
        if button_type == 'header':
            self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)
        elif button_type == 'footer':
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
            self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)