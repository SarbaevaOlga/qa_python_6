import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step('Заполнить первую форму заказа данными пользователя')
    def fill_first_order_form(self, user_data):
        self.set_value(OrderPageLocators.NAME_FIELD, user_data['name'])
        self.set_value(OrderPageLocators.SURNAME_FIELD, user_data['surname'])
        self.set_value(OrderPageLocators.ADDRESS_FIELD, user_data['address'])
        self.set_value(OrderPageLocators.METRO_STATION_FIELD, user_data['metro_station'])
        self.set_value(OrderPageLocators.PHONE_FIELD, user_data['phone'])

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить вторую форму заказа')
    def fill_second_order_form(self, user_data):
        self.set_value(OrderPageLocators.DATE_FIELD, user_data['date'])
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.select_rental_period(user_data['period'])
        self.select_scooter_color(user_data['color'])
        self.set_value(OrderPageLocators.COMMENT_FIELD, user_data['comment'])

    @allure.step('Выбрать период аренды: {period}')
    def select_rental_period(self, period):
        period_locators = {
            'сутки': OrderPageLocators.RENT_PERIOD_1_DAY,
            'двое суток': OrderPageLocators.RENT_PERIOD_2_DAYS,
            'трое суток': OrderPageLocators.RENT_PERIOD_3_DAYS,
            'четверо суток': OrderPageLocators.RENT_PERIOD_4_DAYS,
            'пятеро суток': OrderPageLocators.RENT_PERIOD_5_DAYS,
            'шестеро суток': OrderPageLocators.RENT_PERIOD_6_DAYS,
            'семеро суток': OrderPageLocators.RENT_PERIOD_7_DAYS
        }
        self.click_element(period_locators[period])

    @allure.step('Выбрать цвет самоката: {color}')
    def select_scooter_color(self, color):
        if color == 'black':
            self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click_element(OrderPageLocators.GREY_COLOR_CHECKBOX)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        self.wait_for_element(OrderPageLocators.MODAL_WINDOW)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверить сообщение об успешном заказе')
    def check_success_message(self):
        return self.is_element_present(OrderPageLocators.SUCCESS_MESSAGE)