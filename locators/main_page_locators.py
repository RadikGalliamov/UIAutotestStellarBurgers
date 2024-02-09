from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    - HEADER
    """
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка Конструктор
    PERSONAL_CABINET_TEXT = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор

    """
    - MAIN AREA
    """
    ASSEMBLE_THE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Текст 'Соберите бургер'


    """
    - FOOTER
    """
