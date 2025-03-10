from selenium.webdriver.common.by import By
import locators.base_page_locators


class BasePage:

    button_scooter_start_page = [By.XPATH, locators.base_page_locators.HREF_START_PAGE]
    button_yandex_start_page = [By.XPATH, locators.base_page_locators.HREF_YANDEX_DZEN_PAGE]
    button_order_up = [By.XPATH, locators.base_page_locators.BUTTON_ORDER_UP]

    def __init__(self, driver):
        self.driver = driver

    def click_button_scooter(self):
        self.driver.find_element(*self.button_scooter_start_page).click()

    def click_button_yandex(self):
        self.driver.find_element(*self.button_yandex_start_page).click()
    def click_button_order_up(self):
        self.driver.find_element(*self.button_order_up).click()
