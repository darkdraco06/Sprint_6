from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import locators.order_page_locators
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):
    VERIFICATION_STAUS_ORDER = "Заказ оформлен"
    INPUT_NAME = [By.XPATH, locators.order_page_locators.INPUT_NAME]
    INPUT_LAST_NAME = [By.XPATH, locators.order_page_locators.INPUT_LAST_NAME]
    INPUT_ADDRESS = [By.XPATH, locators.order_page_locators.INPUT_ADDRESS]
    INPUT_METRO_STATION = [By.XPATH, locators.order_page_locators.INPUT_METRO_STATION]
    INPUT_PHONE_NUMBER = [By.XPATH, locators.order_page_locators.INPUT_PHONE_NUMBER]
    BUTTON_NEXT_STEP = [By.XPATH, locators.order_page_locators.BUTTON_NEXT_STEP]
    INPUT_DATE_DELIVERY = [By.XPATH, locators.order_page_locators.INPUT_DATE_DELIVERY]
    INPUT_ARENDA_PERIOD = [By.XPATH, locators.order_page_locators.INPUT_ARENDA_PERIOD]
    INPUT_DROPDOWN_MENU_DAYS = [By.XPATH, locators.order_page_locators.INPUT_DROPDOWN_MENU_DAYS]
    INPUT_COLOR_SCOOTER_BLACK_PERL_ID = [By.ID, locators.order_page_locators.INPUT_COLOR_SCOOTER_BLACK_PERL_ID]
    INPUT_COLOR_SCOOTER_GREY_DEPRESSION_ID = [By.ID,
                                              locators.order_page_locators.INPUT_COLOR_SCOOTER_GREY_DEPRESSION_ID]
    INPUT_COMMIT_FOR_CURER = [By.XPATH, locators.order_page_locators.INPUT_COMMIT_FOR_CURER]
    BUTTON_ORDER_FINISH = [By.XPATH, locators.order_page_locators.BUTTON_ORDER_FINISH]
    MODAL_WINDOW = [By.XPATH, locators.order_page_locators.MODAL_WINDOW]
    MODAL_WINDOW_YES = [By.XPATH, locators.order_page_locators.MODAL_WINDOW_YES]
    MODAL_WINDOW_ORDER_CREATED = [By.XPATH, locators.order_page_locators.MODAL_WINDOW_ORDER_CREATED]
    MODAL_WINDOW_STATUS_ORDER = [By.XPATH, locators.order_page_locators.MODAL_WINDOW_STATUS_ORDER]

    @allure.step('Ввод имени пользователя')
    def set_input_name(self, browser, text):
        self.set_input_data(browser, self.INPUT_NAME, text)

    @allure.step('Ввод фамилии пользователя')
    def set_input_last_name(self, browser, text):
        self.set_input_data(browser, self.INPUT_LAST_NAME, text)

    @allure.step('Ввод адреса пользователя')
    def set_input_address(self, browser, text):
        self.set_input_data(browser, self.INPUT_ADDRESS, text)

    @allure.step('Выбор станции метро')
    def set_input_metro_station(self, browser):
        element = browser.find_element(*self.INPUT_METRO_STATION)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step('Ввод телефона пользователя')
    def set_input_phone_number(self, browser, text):
        self.set_input_data(browser, self.INPUT_PHONE_NUMBER, text)

    @allure.step('Переход на следующий шаг заказа')
    def click_button_next_step(self, browser):
        self.click_element(browser, self.BUTTON_NEXT_STEP)

    @allure.step('Ввод даты доставки самоката')
    def set_input_date_delivery(self, browser, text):
        self.set_input_data(browser, self.INPUT_DATE_DELIVERY, text)

    @allure.step('Выбор дней аренды самоката')
    def set_input_arenda_period(self, browser):
        self.click_element(browser, self.INPUT_ARENDA_PERIOD)
        self.click_element(browser, self.INPUT_DROPDOWN_MENU_DAYS)

    @allure.step('Выбор цвета самоката')
    def click_input_color_scooter_black_perl_id(self, browser):
        self.click_element(browser, self.INPUT_COLOR_SCOOTER_BLACK_PERL_ID)

    @allure.step('Ввод комментария к заказу')
    def set_input_commit_order(self, browser, text):
        self.set_input_data(browser, self.INPUT_COMMIT_FOR_CURER, text)

    @allure.step('Нажатие кнопки заказ самоката')
    def click_button_order_finish(self, browser):
        self.click_element(browser, self.BUTTON_ORDER_FINISH)

    @allure.step('Подтверждение заказа в модальном окне заказа самоката')
    def click_button_modal_window_yes(self, browser):
        self.click_element(browser, self.MODAL_WINDOW_YES)

    @allure.step('Получение текста об успешном заказе самоката из модального окна заказа')
    def get_text_modal_window_status_order(self, browser):
        return self.get_text_element(browser, self.MODAL_WINDOW_ORDER_CREATED)

    @allure.step('Позитивный сценарий создания заказа с заданными параметрами')
    def create_order(self, browser, name, last_name, address, phone_number, date, commit):
        self.click_button_order_up(browser)
        self.set_input_name(browser, name)
        self.set_input_last_name(browser, last_name)
        self.set_input_address(browser, address)
        self.set_input_metro_station(browser)
        self.set_input_phone_number(browser, phone_number)
        self.click_button_next_step(browser)
        self.set_input_date_delivery(browser, date)
        self.set_input_arenda_period(browser)
        self.click_input_color_scooter_black_perl_id(browser)
        self.set_input_commit_order(browser, commit)
        self.click_button_next_step(browser)
        self.click_button_modal_window_yes(browser)
        return self.get_text_modal_window_status_order(browser)
