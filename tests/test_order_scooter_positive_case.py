from pages.order_page import OrderPage
import pytest
import allure

class TestOrderScooter:

    @pytest.mark.parametrize(
        'name,last_name,address,phone_number,date,commit',
        [
            ['Люк', 'Скайуолкер', 'Татуин', '89009008080', '15.03.2025', 'Переходи на темную сторону силы'],
            ['Гарри', 'Поттер', 'Хогвартс', '88008009090', '16.03.2025', 'Гарри твоя палочка!']
        ]
    )
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Переход на страницу заказа происходит с кнопки заказать на главной страницы вверху.'
                        'Проходим полный сценарий с заполнением всех полей валидными значениями.'
                        'Проверяем что заказ создался получив текст "Заказ создан" из элемента модального окна об успешном заказе')
    def test_order_scooter_up_button_all_data_positive_result(self, browser, name, last_name, address, phone_number,
                                                              date, commit):
        order_page = OrderPage()
        status_order = order_page.create_order(browser, name, last_name, address, phone_number, date, commit)
        assert order_page.VERIFICATION_STAUS_ORDER in status_order
