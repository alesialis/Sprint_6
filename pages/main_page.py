from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.loc_main_page import MainPageLocators
from pages.base_page import BasePage
from locators.loc_base_page import BasePageLocators


@allure.step('Определить локатор вопроса')
def loc_questions(number):
    return MainPageLocators.QUESTIONS[number]


@allure.step('Определить локатор ответа')
def loc_answers(number):
    return MainPageLocators.ANSWERS[number]


class MainPage(BasePage):

    @allure.step('Кликнуть на кнопку скрытия уведомления о cookies')
    def confirm_cookies(self):
        self.click(BasePageLocators.BUTTON_CONFIRM_COOKIES)
    @allure.step('Скролл до раздела faq')
    def scroll_to_questions(self):
        self.scroll(MainPageLocators.QUESTIONS[1])

    @allure.step('Ожидание появления раздела faq')
    def wait_for_element(self):
        self.wait_then_find_element(MainPageLocators.QUESTIONS[1])

    @allure.step('Кликнуть на вопрос и получить ответ')
    def click_on_questions(self, number):
        self.wait_then_find_element(loc_questions(number)).click()
        return self.wait_then_find_element(loc_answers(number))

    @allure.step('Клик на кнопку "Заказать" наверху страницы')
    def click_order_button_top(self):
        self.click(MainPageLocators.BUTTON_ORDER_TOP)

    @allure.step('Клик на кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.click(MainPageLocators.BUTTON_ORDER_BOTTOM)

    @allure.step('Клик на лого Яндекс')
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step('Клик на лого Самокат')
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Ожидание заголовка Яндекс Дзен')
    def wait_for_title_dzen(self):
        self.wait_for_title("Дзен")
