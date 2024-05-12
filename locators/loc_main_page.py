from selenium.webdriver.common.by import By
from locators.loc_base_page import BasePageLocators


class MainPageLocators(BasePageLocators):
    # Вопросы на главной в разделе faq
    QUESTIONS = [
        (By.XPATH, "//div[@id='accordion__heading-0']"),
        (By.XPATH, "//div[@id='accordion__heading-1']"),
        (By.XPATH, "//div[@id='accordion__heading-2']"),
        (By.XPATH, "//div[@id='accordion__heading-3']"),
        (By.XPATH, "//div[@id='accordion__heading-4']"),
        (By.XPATH, "//div[@id='accordion__heading-5']"),
        (By.XPATH, "//div[@id='accordion__heading-6']"),
        (By.XPATH, "//div[@id='accordion__heading-7']")
    ]
    # Ответы для каждого вопроса в faq
    ANSWERS = [
        (By.XPATH, "//div[@id='accordion__panel-0']"),
        (By.XPATH, "//div[@id='accordion__panel-1']"),
        (By.XPATH, "//div[@id='accordion__panel-2']"),
        (By.XPATH, "//div[@id='accordion__panel-3']"),
        (By.XPATH, "//div[@id='accordion__panel-4']"),
        (By.XPATH, "//div[@id='accordion__panel-5']"),
        (By.XPATH, "//div[@id='accordion__panel-6']"),
        (By.XPATH, "//div[@id='accordion__panel-7']")
    ]

