from selenium.webdriver.common.by import By


class BasePageLocators:
    # кнопка скрыть уведомления о cookies
    BUTTON_CONFIRM_COOKIES = (By.XPATH, "//*[contains(@class,'App_CookieButton__3cvqF')]")
    # кнопка "Заказать" наверху страницы
    BUTTON_ORDER_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    # кнопка "Заказать" внизу страницы
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    # логотип Яндекс
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    # логотип Самокат
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

