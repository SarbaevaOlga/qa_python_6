from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Поля формы
    NAME_FIELD = (By.CSS_SELECTOR, "[placeholder*='Имя']")
    SURNAME_FIELD = (By.CSS_SELECTOR, "[placeholder*='Фамилия']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "[placeholder*='Адрес']")
    METRO_STATION_FIELD = (By.CSS_SELECTOR, "[placeholder*='Станция метро']")
    PHONE_FIELD = (By.CSS_SELECTOR, "[placeholder*='Телефон']")
    
    # Кнопки
    NEXT_BUTTON = (By.CSS_SELECTOR, "[class*='Button_Middle'][type='button']:first-of-type")
    ORDER_BUTTON = (By.CSS_SELECTOR, "[class*='Button_Middle']:last-of-type")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "[class*='Order_Buttons'] button:first-child")
    
    # Поля второй формы
    DATE_FIELD = (By.CSS_SELECTOR, "[placeholder*='Когда привезти']")
    RENTAL_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "[class*='Dropdown-control']")
    COMMENT_FIELD = (By.CSS_SELECTOR, "[placeholder*='Комментарий']")
    
    # Периоды аренды
    RENT_PERIOD_1_DAY = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(1)")
    RENT_PERIOD_2_DAYS = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(2)")
    RENT_PERIOD_3_DAYS = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(3)")
    RENT_PERIOD_4_DAYS = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(4)")
    RENT_PERIOD_5_DAYS = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(5)")
    RENT_PERIOD_6_DAYS = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(6)")
    RENT_PERIOD_7_DAYS = (By.CSS_SELECTOR, "[class*='Dropdown-option']:nth-child(7)")
    
    # Цвета
    BLACK_COLOR_CHECKBOX = (By.CSS_SELECTOR, "[for='black']")
    GREY_COLOR_CHECKBOX = (By.CSS_SELECTOR, "[for='grey']")
    
    # Модальное окно
    MODAL_WINDOW = (By.CSS_SELECTOR, "[class*='Order_Modal']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[class*='Order_Modal'] [class*='Order_Text']")