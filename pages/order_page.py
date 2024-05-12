import allure
from locators.loc_order_page import OrderPageLocators
from pages.base_page import BasePage
from datetime import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    @allure.step("Ввести данные пользователя на форме")
    def type_customer_data(self, customer_data):
        # ввести имя
        name = self.wait_then_find_element(OrderPageLocators.FIELD_NAME)
        name.send_keys(customer_data["name"])
        # ввести фамилию
        surname = self.wait_then_find_element(OrderPageLocators.FIELD_SURNAME)
        surname.send_keys(customer_data["surname"])
        # ввести адрес
        address = self.wait_then_find_element(OrderPageLocators.FIELD_ADDRESS)
        address.send_keys(customer_data["address"])
        # ввести метро
        subway = self.wait_then_find_element(OrderPageLocators.FIELD_SUBWAY)
        subway.click()
        subway.send_keys(customer_data["subway"])
        subway_selected = self.wait_then_find_element(OrderPageLocators.SELECTED_SUBWAY)
        subway_selected.click()
        # Ввод телефона
        phone = self.wait_then_find_element(OrderPageLocators.FIELD_PHONE)
        phone.send_keys(customer_data["phone"])

    @allure.step("Клик по кнопке Далее - переход к форме аренды")
    def go_to_rent_form(self):
        self.wait_then_find_element(OrderPageLocators.BUTTON_NEXT_TO_RENT).click()

    @allure.step("Ввести данные об аренде самоката")
    def type_rent_data(self, customer_data):
        # ввести текущую дату
        date = self.wait_then_find_element(OrderPageLocators.FIELD_DATE)
        current_date = datetime.today()
        current_date = current_date.strftime("%d.%m.%Y")
        date.send_keys(current_date)
        date.send_keys(Keys.ENTER)
        # ввести период аренды
        period = self.wait_then_find_element(OrderPageLocators.FIELD_PERIOD)
        period.click()
        period_selected = self.wait_then_find_element([By.XPATH, f".//*[text()='{customer_data["period"]}']"])
        period_selected.click()
        # ввести цвет
        colour = self.wait_then_find_element([By.XPATH, f".//*[text()='{customer_data["scooter_colour"]}']"])
        colour.click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        # клик по "Заказать"
        self.wait_then_find_element(OrderPageLocators.BUTTON_ORDER).click()
        # подтвердить
        self.wait_then_find_element(OrderPageLocators.BUTTON_YES).click()

    @allure.step("Ожидание текста о подтверждении")
    def wait_for_text_confirmed(self):
        self.wait_then_find_element(OrderPageLocators.TEXT_ORDER_CONFIRMED)

    @allure.step("Ожидание текста о подтверждении")
    def get_text_confirmed(self):
        text_confirmed = self.wait_then_find_element(OrderPageLocators.TEXT_ORDER_CONFIRMED)
        return text_confirmed.text if text_confirmed else None




