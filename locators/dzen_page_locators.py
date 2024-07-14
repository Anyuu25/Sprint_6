from selenium.webdriver.common.by import By


class DzenPageLocators:
    MAIN_BUTTON_DZEN = (By.XPATH, ".//span[text() = 'Главная']")
    LOGO_DZEN = (By.XPATH, ".//a[@class = 'desktop-base-header__logoLink-2h']")