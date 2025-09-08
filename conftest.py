import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    # Настраиваем Firefox
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)

    driver.set_window_size(1200, 800)
    browser.config.driver = driver
    browser.config.base_url = 'https://google.com'
    browser.config.timeout = 10

    yield

    browser.quit()