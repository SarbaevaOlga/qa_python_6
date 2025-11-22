from selenium.webdriver.common.by import By

class MainPageLocators:
    # Новые локаторы для кнопок заказа
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, "[class*='Button_Button__ra12g']:first-of-type")
    ORDER_BUTTON_FOOTER = (By.CSS_SELECTOR, "[class*='Button_Middle__1CSJM']")
    
    # Локаторы для логотипов
    SCOOTER_LOGO = (By.CSS_SELECTOR, "[class*='Header_LogoScooter__']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "[class*='Header_LogoYandex__']")
    
    # Локаторы для FAQ
    QUESTION_LOCATOR_TEMPLATE = "[data-accordion-component='AccordionItemButton'][id='accordion__heading-{}']"
    ANSWER_LOCATOR_TEMPLATE = "[data-accordion-component='AccordionItemPanel'][id='accordion__panel-{}']"
    
    # Локатор для куки
    COOKIE_BUTTON = (By.CSS_SELECTOR, "[class*='App_CookieButton']")