from selenium.webdriver.common.by import By


class LoginPageLocators:

    """
    - MAIN AREA
    """
    ENTER_TEXT = (By.XPATH, ".//h2[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")  # Поле 'Email'
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")  # Поле 'Пароль'
    ENTER = (By.XPATH, ".//button[text()='Войти']")  # Кнопка 'Войти'

    TEXT_RECOVER_PASSWORD = (By.XPATH, ".//a[@class='Auth_link__1fOlj'][text()='Восстановить пароль']")