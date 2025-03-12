from selenium.webdriver.common.by import By
import locators.base_page_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:
    BUTTON_SCOOTER_START_PAGE = [By.XPATH, locators.base_page_locators.HREF_START_PAGE]
    BUTTON_YANDEX_START_PAGE = [By.XPATH, locators.base_page_locators.HREF_YANDEX_DZEN_PAGE]
    BUTTON_ORDER_UP = [By.XPATH, locators.base_page_locators.BUTTON_ORDER_UP]

    @allure.step('Ожидание загрузки выбранного элемента')
    def wait_for_load_element(self, browser, element):
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Нажатие кнопки "Заказать" в верху страницы')
    def click_button_order_up(self, browser):
        browser.find_element(*self.BUTTON_ORDER_UP).click()

    @allure.step('Прокрутка до выбранного элемента')
    def scroll_to_element(self, browser, find_element):
        element = browser.find_element(*find_element)
        browser.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Клик по выбранному элементу')
    def click_element(self, browser, find_element):
        browser.find_element(*find_element).click()

    @allure.step('Получение текста выбранного элемента')
    def get_text_element(self, browser, find_element):
        return browser.find_element(*find_element).text

    @allure.step('Поиск выбранного элемента')
    def find_element_on_page(self, browser, find_element):
        browser.find_element(*find_element)

    @allure.step('Ввод выбранных значений в поле')
    def set_input_data(self, browser, find_element, data):
        browser.find_element(*find_element).send_keys(data)
