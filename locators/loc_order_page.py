from selenium.webdriver.common.by import By
from locators.loc_base_page import BasePageLocators


class OrderPageLocators(BasePageLocators):
    # имя
    FIELD_NAME = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    # фамилия
    FIELD_SURNAME = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    # адрес
    FIELD_ADDRESS = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    # метро
    FIELD_SUBWAY = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    # телефон
    FIELD_PHONE = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    # кнопка Далее - к форме аренды
    BUTTON_NEXT_TO_RENT = [By.XPATH, ".//button[text() = 'Далее']"]
    # дата
    FIELD_DATE = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    # период
    FIELD_PERIOD = [By.XPATH, ".//div[@class = 'Dropdown-control']"]
    # цвет
    CHECKBOX_COLOUR = [By.XPATH, ".//label[1]/input[@class = 'Checkbox_Input__14A2w']"]
    # кнопка Заказать
    BUTTON_ORDER = [By.XPATH, ".//button[2][text() = 'Заказать']"]
    # кнопка "да" для подтверждения
    BUTTON_YES = [By.XPATH, ".//button[2][text() = 'Да']"]
    # текст о завершении оформления заказа
    TEXT_ORDER_CONFIRMED = [By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']"]
    # выбранная станция метро
    SELECTED_SUBWAY = [By.CLASS_NAME, 'select-search__select']
