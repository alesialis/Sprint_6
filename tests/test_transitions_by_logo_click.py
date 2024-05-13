import allure
from conftest import driver
from pages.main_page import MainPage


class TestTransitions:
    @allure.title('Переход на Яндекс Дзен по клику на лого Яндекса')
    @allure.description('При клике по логотипу открывается страница Дзен')
    def test_transition_by_yandex_logo(self, driver):
        main_page = MainPage(driver)
        # скрыть уведомление о cookies
        main_page.confirm_cookies()
        # кликнуть на лого Яндекса
        main_page.click_yandex_logo()
        # переключить драйвер
        main_page.switch_driver()
        # ожидание заголовка при открытии страницы
        main_page.wait_for_title_dzen()
        # проверка текущей страницы
        assert 'dzen' in main_page.get_current_url()

    @allure.title('Переход на Яндекс Дзен по клику на лого Самокат')
    @allure.description('При клике по логотипу открывается страница Дзен')
    def test_transition_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        # скрыть уведомление о cookies
        main_page.confirm_cookies()
        # url главной страницы Самоката
        before_url = main_page.get_current_url()
        # переход по клику на "Заказать"
        main_page.click_order_button_top()
        # кликнуть на лого Самоката
        main_page.click_scooter_logo()
        # url страницы по клику на лого Самоката
        after_url = main_page.get_current_url()
        # проверка перехода на главную
        assert before_url == after_url

