from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import locators.start_page_locators
import allure


class StartPage(BasePage):
    ELEMENT_BUTTON_MIDDEL_ORDER = [By.XPATH, locators.start_page_locators.BUTTON_ORDER_MIDDEL]

    ELEMENT_QUESTION_PRICE = [By.ID, locators.start_page_locators.QUESTION_PRICE]
    ELEMENT_QUESTION_WANT_SCOOTER = [By.ID, locators.start_page_locators.QUESTION_WANT_SCOOTER]
    ELEMENT_QUESTION_CALCULATION_RENT = [By.ID, locators.start_page_locators.QUESTION_CALCULATION_RENT]
    ELEMENT_QUESTION_ORDER_TODAY = [By.ID, locators.start_page_locators.QUESTION_ORDER_TODAY]
    ELEMENT_QUESTION_RETURN_SCOOTER = [By.ID, locators.start_page_locators.QUESTION_RETURN_SCOOTER]
    ELEMENT_QUESTION_CHARGING_SCOOTER = [By.ID, locators.start_page_locators.QUESTION_CHARGING_SCOOTER]
    ELEMENT_QUESTION_CANSEL_ORDER = [By.ID, locators.start_page_locators.QUESTION_CANSEL_ORDER]
    ELEMENT_QUESTION_IF_MKAD_LIFE = [By.ID, locators.start_page_locators.QUESTION_IF_MKAD_LIFE]

    ELEMENT_ANSWER_PRICE = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_PRICE]
    ELEMENT_ANSWER_WANT_SCOOTER = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_WANT_SCOOTER]
    ELEMENT_ANSWER_CALCULATION_RENT = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_CALCULATION_RENT]
    ELEMENT_ANSWER_ORDER_TODAY = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_ORDER_TODAY]
    ELEMENT_ANSWER_RETURN_SCOOTER = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_RETURN_SCOOTER]
    ELEMENT_ANSWER_CHARGING_SCOOTER = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_CHARGING_SCOOTER]
    ELEMENT_ANSWER_CANSEL_ORDER = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_CANSEL_ORDER]
    ELEMENT_ANSWER_IF_MKAD_LIFE = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_IF_MKAD_LIFE]

    VERIFICATION_TEXT_PRICE = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    VERIFICATION_TEXT_WANT_SCOOTER = ("Пока что у нас так: один заказ — один самокат. "
                                      "Если хотите покататься с друзьями, можете просто сделать несколько заказов — "
                                      "один за другим.")
    VERIFICATION_TEXT_CALCULATION_RENT = (
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
    VERIFICATION_TEXT_ORDER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    VERIFICATION_TEXT_RETURN_SCOOTER = (
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")
    VERIFICATION_TEXT_CHARGING_SCOOTER = ("Самокат приезжает к вам с полной зарядкой. "
                                          "Этого хватает на восемь суток — даже если будете кататься без передышек и "
                                          "во сне. "
                                          "Зарядка не понадобится.")
    VERIFICATION_TEXT_CANSEL_ORDER = (
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. "
        "Все же свои.")
    VERIFICATION_TEXT_IF_MKAD_LIFE = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


    VERIFICATION_URL_YANDEX = "https://dzen.ru/?yredirect=true"
    VERIFICATION_URL_SCOOTER_ORDER_PAGE = "https://qa-scooter.praktikum-services.ru/order"
    VERIFICATION_URL_SCOOTER_START_PAGE = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Получение текста ответа на выбранный вопрос')
    def get_text_element_answer(self, browser, question, answer):
        self.wait_for_load_element(browser, question)
        self.scroll_to_element(browser, question)
        self.wait_for_load_element(browser, question)
        self.click_element(browser, question)
        self.wait_for_load_element(browser, answer)
        return self.get_text_element(browser, answer)

    @allure.step('Клик по кнопке Заказать внизу стартовой странице')
    def order_button_middel_order(self, browser):
        self.scroll_to_element(browser, self.ELEMENT_BUTTON_MIDDEL_ORDER)
        self.click_element(browser, self.ELEMENT_BUTTON_MIDDEL_ORDER)

    @allure.step('Переход по кнопке Яндекс на стартовую страницу ЯндексДзен')
    def go_to_yandex_page(self, browser):
        self.click_element(browser, self.BUTTON_YANDEX_START_PAGE)

    @allure.step('Переход по кнопке Самокат на стартовую страницу Самокат')
    def go_to_scooter_page(self, browser):
        self.click_element(browser, self.BUTTON_SCOOTER_START_PAGE)



