import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope='function')
def driver(request):
    """
    Фикстура для инициализации и закрытия браузера
    """
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        if headless:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f'Unsupported browser: {browser}')
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    """
    Добавление кастомных опций для pytest
    """
    parser.addoption(
        '--browser', 
        action='store', 
        default='chrome', 
        help='Browser to run tests: chrome or firefox'
    )
    parser.addoption(
        '--headless',
        action='store_true',
        default=False,
        help='Run tests in headless mode'
    )