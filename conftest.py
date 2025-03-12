import pytest
from selenium import webdriver

import datetime

tomorrow = (datetime.date.today() + datetime.timedelta(days=2)).strftime('%d.%m.%Y')


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
