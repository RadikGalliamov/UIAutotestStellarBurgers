from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    """
    - MAIN AREA
    """
    """Текст 'Восстановление пароля'"""
    TEXT_PASSWORD_RECOVERY = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Восстановление пароля']")
    """Поле ввода email"""
    FIELD_EMAIL = (By.XPATH, ".//input[@name='name']")
    """Кнопка 'Восстановить'"""
    BUTTON_RECOVER = (By.XPATH, ".//button[text()='Восстановить']")
    """Поле 'Пароль'"""
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Введите новый пароль']")
    """Поле 'Введите код из письма'"""
    FIELD_ENTER_THE_CODE_FROM_THE_LETTER = (
        By.XPATH, "//input[@name='name']/preceding-sibling::label[text()='Введите код из письма']")
    """Символ 'глаз' - скрыть/показать пароль"""
    EYE_ACTIVE = (By.XPATH, ".//div[@class='input__icon input__icon-action']")

    FIELD_PASSWORD_IS_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")





