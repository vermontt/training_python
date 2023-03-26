import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeopt


@pytest.fixture
def chrome_options():
    options = chromeopt()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(chrome_options):
    options = chrome_options
    driver = webdriver.Chrome(executable_path='C:\ChromeDriver/chromedriver.exe', options=options)
    return driver


@pytest.fixture(scope="function")
def setup(get_webdriver):
    driver = get_webdriver
    driver.get('https://www.mvideo.ru/')
    yield driver
    driver.quit()
