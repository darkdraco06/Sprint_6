from pages.start_page import StartPage
import pytest
import allure


class TestImportantQuestions(StartPage):

    @pytest.mark.parametrize(
        'questions,answer,verification_text',
        [
            [StartPage.ELEMENT_QUESTION_PRICE, StartPage.ELEMENT_ANSWER_PRICE, StartPage.VERIFICATION_TEXT_PRICE],
            [StartPage.ELEMENT_QUESTION_WANT_SCOOTER, StartPage.ELEMENT_ANSWER_WANT_SCOOTER, StartPage.VERIFICATION_TEXT_WANT_SCOOTER],
            [StartPage.ELEMENT_QUESTION_CALCULATION_RENT, StartPage.ELEMENT_ANSWER_CALCULATION_RENT, StartPage.VERIFICATION_TEXT_CALCULATION_RENT],
            [StartPage.ELEMENT_QUESTION_ORDER_TODAY, StartPage.ELEMENT_ANSWER_ORDER_TODAY, StartPage.VERIFICATION_TEXT_ORDER_TODAY],
            [StartPage.ELEMENT_QUESTION_RETURN_SCOOTER, StartPage.ELEMENT_ANSWER_RETURN_SCOOTER, StartPage.VERIFICATION_TEXT_RETURN_SCOOTER],
            [StartPage.ELEMENT_QUESTION_CHARGING_SCOOTER, StartPage.ELEMENT_ANSWER_CHARGING_SCOOTER, StartPage.VERIFICATION_TEXT_CHARGING_SCOOTER],
            [StartPage.ELEMENT_QUESTION_CANSEL_ORDER, StartPage.ELEMENT_ANSWER_CANSEL_ORDER, StartPage.VERIFICATION_TEXT_CANSEL_ORDER],
            [StartPage.ELEMENT_QUESTION_IF_MKAD_LIFE, StartPage.ELEMENT_ANSWER_IF_MKAD_LIFE, StartPage.VERIFICATION_TEXT_IF_MKAD_LIFE]
        ]
    )
    @allure.title('Проверка соответствия текста ответа на вопросы на стартовой странице')
    @allure.description('На странице ищем элемент "Вопрос", получаем текст овтета и сравниваем его с текстом ответа для проверки')
    def test_verification_text_answer_eight_questions_positive_result(self, browser, questions, answer, verification_text):
        assert verification_text == self.get_text_element_answer(browser, questions, answer)
