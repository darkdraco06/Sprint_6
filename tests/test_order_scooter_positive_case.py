from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
import pytest



class TestOrderScooter:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'name,last_name,address,phone_number,date,commit',
        [
            ['Люк', 'Скайуолкер', 'Татуин', '89009008080', '15.03.2025', 'Переходи на темную сторону силы'],
            ['Гарри', 'Поттер', 'Хогвартс', '88008009090', '16.03.2025', 'Гарри твоя палочка!']
        ]
    )

    def test_order_scooter_up_button_all_data_positive_result(self, name, last_name, address, phone_number, date, commit):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.click_button_order_up()
        order_page.create_order(name, last_name, address, phone_number, date, commit)
        status_order = order_page.get_text_modal_window_status_order()
        assert "Заказ оформлен" in status_order

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
