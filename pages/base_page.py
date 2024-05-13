from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.loc_base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Запросить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключить драйвер')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание и обнаружение конкретного элемента на странице')
    def wait_then_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание изменения URL')
    def wait_for_url_change(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(url))

    @allure.step('Кликнуть по конкретному элементу')
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скролл до нужного элемента')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание заголовка')
    def wait_for_title(self, title):
        WebDriverWait(self.driver, 5).until(expected_conditions.title_is(title))
