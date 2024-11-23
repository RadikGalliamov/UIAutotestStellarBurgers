import allure
from selenium.webdriver.common.by import By
from data import TestForgotPasswordData

from pages.base_page import BasePage


class ForgotPasswordPageHelper(BasePage):
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

    @allure.step("Найти и заполнить поле 'Email', ввести почтовый адрес и кликнуть кнопку 'Восстановить'")
    def find_and_enter_field_mail_address(self, email):
        email_field = self._wait_for_clickable(locator=self.FIELD_EMAIL)
        email_field.send_keys(email)

    @allure.step("Найти и кликнуть кнопку 'Восстановить'")
    def find_and_click_recovery_button(self):
        self._wait_for_clickable(locator=self.BUTTON_RECOVER).click()

    @allure.step("Найти, кликнуть по полю 'Пароль' и ввести пароль")
    def find_click_and_input_password_in_field_password(self):
        self._wait_for_clickable(locator=self.FIELD_PASSWORD).click()
        self._wait_for_visibility(
            locator=self.FIELD_PASSWORD).send_keys(TestForgotPasswordData.password)

    @allure.step("Найти в поле 'Пароль' значок 'Глаз' кликнуть по нему")
    def find_element_eye_and_click(self):
        self._find_element(locator=self.EYE_ACTIVE).click()

    @allure.step("Найти поле 'Введите код из письма'")
    def find_field_enter_pass_from_mail(self):
        return self._find_element(locator=self.FIELD_ENTER_THE_CODE_FROM_THE_LETTER)

    @allure.step("Найти активное поле 'Пароль'")
    def find_field_active_field_password(self):
        return self._find_element(locator=self.FIELD_PASSWORD_IS_ACTIVE)
