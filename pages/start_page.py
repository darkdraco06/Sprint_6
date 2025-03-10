from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.start_page_locators


class StartPageScooter:
    element_button_middel_order = [By.XPATH, locators.start_page_locators.BUTTON_ORDER_MIDDEL]

    element_question_price = [By.ID, locators.start_page_locators.QUESTION_PRICE]
    element_question_want_scooter = [By.ID, locators.start_page_locators.QUESTION_WANT_SCOOTER]
    element_question_calculation_rent = [By.ID, locators.start_page_locators.QUESTION_CALCULATION_RENT]
    element_question_order_today = [By.ID, locators.start_page_locators.QUESTION_ORDER_TODAY]
    element_question_return_scooter = [By.ID, locators.start_page_locators.QUESTION_RETURN_SCOOTER]
    element_question_charging_scooter = [By.ID, locators.start_page_locators.QUESTION_CHARGING_SCOOTER]
    element_question_cansel_order = [By.ID, locators.start_page_locators.QUESTION_CANSEL_ORDER]
    element_question_if_mkad_life = [By.ID, locators.start_page_locators.QUESTION_IF_MKAD_LIFE]

    element_answer_price = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_PRICE]
    element_answer_want_scooter = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_WANT_SCOOTER]
    element_answer_calculation_rent = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_CALCULATION_RENT]
    element_answer_order_today = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_ORDER_TODAY]
    element_answer_return_scooter = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_RETURN_SCOOTER]
    element_answer_charging_scooter = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_CHARGING_SCOOTER]
    element_answer_cansel_order = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_CANSEL_ORDER]
    element_answer_if_mkad_life = [By.XPATH, locators.start_page_locators.TEXT_ANSWER_IF_MKAD_LIFE]

    VERIFICATION_TEXT_PRICE = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    VERIFICATION_TEXT_WANT_SCOOTER = ("Пока что у нас так: один заказ — один самокат. "
                                      "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")
    VERIFICATION_TEXT_CALCULATION_RENT = (
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
    VERIFICATION_TEXT_ORDER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    VERIFICATION_TEXT_RETURN_SCOOTER = (
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")
    VERIFICATION_TEXT_CHARGING_SCOOTER = ("Самокат приезжает к вам с полной зарядкой. "
                                          "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
                                          "Зарядка не понадобится.")
    VERIFICATION_TEXT_CANSEL_ORDER = (
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. "
        "Все же свои.")
    VERIFICATION_TEXT_IF_MKAD_LIFE = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_element(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element))

    def scroll_to_element(self, find_element):
        element = self.driver.find_element(*find_element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element_in_question_block(self, question):
        self.driver.find_element(*question).click()

    def click_button_order_middel(self):
        self.driver.find_element(*self.element_button_middel_order).click()

    def set_text_element_answer(self, question, answer):
        self.wait_for_load_element(question)
        self.scroll_to_element(question)
        self.wait_for_load_element(question)
        self.click_element_in_question_block(question)
        self.wait_for_load_element(answer)
        return self.driver.find_element(*answer).text
