import pytest
import allure
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
import data


class TestMakeOrder:
    @allure.title('Оформление заказа по клику на кнопку "Заказать" наверху страницы')
    @allure.description('Позитивная проверка: Оформление заказа с двумя наборами данных')
    @pytest.mark.parametrize('customer_data', [data.TEST_USER_1, data.TEST_USER_2])
    def test_make_order_by_top_button(self, driver, customer_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # скрыть уведомление о cookies
        main_page.confirm_cookies()
        # клик по верхней кнопке "Заказать"
        main_page.click_order_button_top()
        # ввести данные пользователя
        order_page.type_customer_data(customer_data)
        # клик по кнопке "Далее"
        order_page.go_to_rent_form()
        # ввести данные аренды
        order_page.type_rent_data(customer_data)
        # клик по кнопке "Заказать"
        order_page.confirm_order()
        # проверка оформления
        order_page.wait_for_text_confirmed()
        assert "Заказ оформлен" in order_page.get_text_confirmed()
