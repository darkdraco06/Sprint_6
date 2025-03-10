from selenium import webdriver
from pages.start_page import StartPageScooter



class TestImportantQuestions:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_important_questions_text_price_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_price, start_page.element_answer_price)
        assert text_answer == start_page.VERIFICATION_TEXT_PRICE

    def test_text_important_questions_text_want_scooter_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_want_scooter, start_page.element_answer_want_scooter)
        assert text_answer == start_page.VERIFICATION_TEXT_WANT_SCOOTER

    def test_text_important_questions_text_calculation_rent_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_calculation_rent, start_page.element_answer_calculation_rent)
        assert text_answer == start_page.VERIFICATION_TEXT_CALCULATION_RENT

    def test_text_important_questions_text_order_today_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_order_today, start_page.element_answer_order_today)
        assert text_answer == start_page.VERIFICATION_TEXT_ORDER_TODAY

    def test_text_important_questions_text_return_scooter_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_return_scooter, start_page.element_answer_return_scooter)
        assert text_answer == start_page.VERIFICATION_TEXT_RETURN_SCOOTER

    def test_text_important_questions_text_charging_scooter_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_charging_scooter, start_page.element_answer_charging_scooter)
        assert text_answer == start_page.VERIFICATION_TEXT_CHARGING_SCOOTER

    def test_text_important_questions_text_cansel_order_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_cansel_order, start_page.element_answer_cansel_order)
        assert text_answer == start_page.VERIFICATION_TEXT_CANSEL_ORDER

    def test_text_important_questions_text_question_if_mkad_life_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        start_page = StartPageScooter(self.driver)
        text_answer = start_page.set_text_element_answer(start_page.element_question_if_mkad_life, start_page.element_answer_if_mkad_life)
        assert text_answer == start_page.VERIFICATION_TEXT_IF_MKAD_LIFE

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()


