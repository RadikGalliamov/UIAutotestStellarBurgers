from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    - HEADER
    """
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_CABINET_TEXT = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы

    """
    - MAIN AREA
    """


    """
    - FOOTER
    """
