"""The module contains fixtures for test functions"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def get_driver() -> WebDriver:
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function',
                params=[('created', 'Created'), ('no-content', 'No Content'), ('moved', 'Moved Permanently'),
                        ('bad_request', 'Bad Request'), ('fordidden', 'Forbidden'), ('not_found', 'Not Found')])
def get_response_type_and_answer(request):
    data = request.param
    return data

