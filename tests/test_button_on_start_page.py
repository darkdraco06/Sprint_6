from pages.start_page import StartPage
import time
import allure


class TestButtonStartPage(StartPage):

    @allure.title('Проверка работы кнопки "Заказать" в низу стартовой страницы')
    @allure.description('Кликаем на кнопку "Заказать" и проверяем что мы перешли на страницу создания заказа')
    def test_button_order_middel_positive_result(self, browser):
        self.order_button_middel_order(browser)
        assert browser.current_url == self.VERIFICATION_URL_SCOOTER_ORDER_PAGE

    @allure.title('Проверка работы кнопки "Яндекс"')
    @allure.description('Кликаем на кнопку "Яндекс" и проверяем что мы перешли на  страницу ЯндексДзен')
    def test_button_yandex_positive_result(self, browser):
        self.go_to_yandex_page(browser)
        time.sleep(3)
        handles = browser.window_handles
        browser.switch_to.window(handles[-1])
        assert browser.current_url == self.VERIFICATION_URL_YANDEX

    @allure.title('Проверка работы кнопки "Самокат"')
    @allure.description('Кликаем на кнопку "Заказать". Переходим на страницу заказа с кликаем на кнопку "Самокат".'
                        'Проверяем что мы перешли на стартовую страницу сайта Самокат')
    def test_button_scooter_positive_result(self, browser):
        self.order_button_middel_order(browser)
        self.go_to_scooter_page(browser)
        assert browser.current_url == self.VERIFICATION_URL_SCOOTER_START_PAGE

