import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selene import browser, be, have


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)

    browser.config.driver = driver
    browser.config.base_url = 'https://ya.ru'
    browser.config.timeout = 15
    browser.config.window_width = 1200
    browser.config.window_height = 800

    yield
    browser.quit()