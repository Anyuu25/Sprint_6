from selenium.webdriver.common.by import By


class DzenPageLocators:
    main_button_dzen = (By.XPATH, ".//span[text() = 'Главная']")
    logo_dzen = (By.XPATH, ".//a[@class = 'desktop-base-header__logoLink-2h']")