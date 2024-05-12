import pytest
import allure
from conftest import driver
from data import answers
from pages.main_page import MainPage


class TestQuestionsOnMainPage:
    @allure.title('Корректные ответы на вопросы в разделе "Вопросы о важном" на главной')
    @allure.description('Проверка всех ответов при клике на вопросы')
    @pytest.mark.parametrize('question', answers)
    def test_get_answers_on_main_page(self, driver, question):
        number, question = question
        main_page = MainPage(driver)

        # скрыть уведомление о cookies
        main_page.confirm_cookies()
        # скролл до faq
        main_page.scroll_to_questions()
        # ожидание раздела
        main_page.wait_for_element()
        # клик на вопросы и получение ответов
        main_page.click_on_questions(number)
        # сопоставить ответ каждому вопросу
        assert main_page.click_on_questions(number).text == question

