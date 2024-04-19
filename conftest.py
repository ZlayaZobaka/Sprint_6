import pytest
import data.urls as urls
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    """
    Вебдрайвер Firefox
    """

    driver = webdriver.Firefox()
    driver.get(urls.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
