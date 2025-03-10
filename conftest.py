import pytest
from selenium import webdriver
import random
import datetime

tomorrow = (datetime.date.today() + datetime.timedelta(days=2)).strftime('%d.%m.%Y')


@pytest.fixture
def data_order_1():
    return {
        "name": "Глаша",
        "last_name": "Скайволкер",
        "address": "Татуин",
        "phone_number": f"8{random.randint(1000000000, 9999999999)}",
        "date": f"{tomorrow}",
        "commit": "Почувствуй потоки силы"
    }
@pytest.fixture
def data_order_2():
    return {
        "name": "Демьян",
        "last_name": "Вейдар",
        "address": "ЗвездаСмерти",
        "phone_number": f"8{random.randint(1000000000, 9999999999)}",
        "date": f"{tomorrow}",
        "commit": "Переходи на темную сторону"
    }
