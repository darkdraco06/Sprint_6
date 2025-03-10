from selenium.webdriver.common.by import By
import locators.order_page_locators
from selenium.webdriver.common.keys import Keys
import time


class OrderPage:

    input_name = [By.XPATH, locators.order_page_locators.INPUT_NAME]
    input_last_name = [By.XPATH, locators.order_page_locators.INPUT_LAST_NAME]
    input_address = [By.XPATH, locators.order_page_locators.INPUT_ADDRESS]
    input_metro_station = [By.XPATH, locators.order_page_locators.INPUT_METRO_STATION]
    input_phone_number = [By.XPATH, locators.order_page_locators.INPUT_PHONE_NUMBER]
    button_next_step = [By.XPATH, locators.order_page_locators.BUTTON_NEXT_STEP]
    input_date_delivery = [By.XPATH, locators.order_page_locators.INPUT_DATE_DELIVERY]
    input_arenda_period = [By.XPATH, locators.order_page_locators.INPUT_ARENDA_PERIOD]
    input_dropdown_menu_days = [By.XPATH, locators.order_page_locators.INPUT_DROPDOWN_MENU_DAYS]
    input_color_scooter_black_perl_id = [By.ID, locators.order_page_locators.INPUT_COLOR_SCOOTER_BLACK_PERL_ID]
    input_color_scooter_grey_depression_id = [By.ID, locators.order_page_locators.INPUT_COLOR_SCOOTER_GREY_DEPRESSION_ID]
    input_commit_for_curer =[By.XPATH, locators.order_page_locators.INPUT_COMMIT_FOR_CURER]
    button_order_finish = [By.XPATH, locators.order_page_locators.BUTTON_ORDER_FINISH]
    modal_window = [By.XPATH, locators.order_page_locators.MODAL_WINDOW]
    modal_window_yes = [By.XPATH, locators.order_page_locators.MODAL_WINDOW_YES]
    modal_window_order_created = [By.XPATH, locators.order_page_locators.MODAL_WINDOW_ORDER_CREATED]
    modal_window_status_order = [By.XPATH, locators.order_page_locators.MODAL_WINDOW_STATUS_ORDER]

    def __init__(self, driver):
        self.driver = driver

    def click_input_name(self):
        self.driver.find_element(*self.input_name).click()

    def set_input_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    def click_input_last_name(self):
        self.driver.find_element(*self.input_last_name).click()

    def set_input_last_name(self, last_name):
        self.driver.find_element(*self.input_last_name).send_keys(last_name)

    def click_input_address(self):
        self.driver.find_element(*self.input_address).click()

    def set_input_address(self, address):
        self.driver.find_element(*self.input_address).send_keys(address)

    def click_input_metro_station(self):
        self.driver.find_element(*self.input_metro_station).click()

    def set_input_metro_station(self):
        element = self.driver.find_element(*self.input_metro_station)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def click_input_phone_number(self):
        self.driver.find_element(*self.input_phone_number).click()

    def set_input_phone_number(self, phone_number):
        self.driver.find_element(*self.input_phone_number).send_keys(phone_number)

    def click_button_next_step(self):
        self.driver.find_element(*self.button_next_step).click()

    def set_input_date_delivery(self, date):
        self.driver.find_element(*self.input_date_delivery).send_keys(date)

    def click_input_arenda_period(self):
        self.driver.find_element(*self.input_arenda_period).click()

    def set_input_arenda_period(self):
        self.driver.find_element(*self.input_dropdown_menu_days).click()

    def click_input_color_scooter_black_perl_id(self):
        self.driver.find_element(*self.input_color_scooter_black_perl_id).click()

    def set_input_commit_order(self, commit):
        self.driver.find_element(*self.input_commit_for_curer).send_keys(commit)

    def click_button_order_finish(self):
        self.driver.find_element(*self.button_order_finish).click()

    def click_button_modal_window_yes(self):
        self.driver.find_element(*self.modal_window_yes).click()

    def get_text_modal_window_status_order(self):
        return self.driver.find_element(*self.modal_window_order_created).text

    def create_order(self, name, last_name, address, phone_number, date, commit):
        self.set_input_name(name)
        self.set_input_last_name(last_name)
        self.set_input_address(address)
        self.set_input_metro_station()
        self.set_input_phone_number(phone_number)
        self.click_button_next_step()
        self.set_input_date_delivery(date)
        self.click_input_arenda_period()
        self.set_input_arenda_period()
        self.click_input_color_scooter_black_perl_id()
        self.set_input_commit_order(commit)
        self.click_button_next_step()
        self.click_button_modal_window_yes()



