from selenium import webdriver
from pages.base_page import BasePage
from pages.start_page import StartPageScooter
import time


class TestButtonStartPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_button_order_middel_positive_result(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        start_page.scroll_to_element(start_page.element_button_middel_order)
        start_page.click_button_order_middel()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    def test_button_yandex_positive_result(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.click_button_yandex()
        time.sleep(3)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

        assert self.driver.current_url == "https://dzen.ru/?yredirect=true"

    def test_button_scooter_positive_result(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.click_button_order_up()
        base_page.click_button_scooter()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
