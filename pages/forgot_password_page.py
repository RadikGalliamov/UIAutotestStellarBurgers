import allure

from data import TestForgotPasswordData
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPageHelper(BasePage):
    @allure.step("Найти и заполнить поле 'Email', ввести почтовый адрес и кликнуть кнопку 'Восстановить'")
    def find_and_enter_field_mail_address(self, email):
        email_field = self.wait_for_clickable(locator=ForgotPasswordPageLocators.FIELD_EMAIL)
        email_field.send_keys(email)

    @allure.step("Найти и кликнуть кнопку 'Восстановить'")
    def find_and_click_recovery_button(self):
        self.wait_for_clickable(locator=ForgotPasswordPageLocators.BUTTON_RECOVER).click()

    @allure.step("Найти, кликнуть по полю 'Пароль' и ввести пароль")
    def find_click_and_input_password_in_field_password(self):
        self.wait_for_clickable(locator=ForgotPasswordPageLocators.FIELD_PASSWORD).click()
        self.wait_for_visibility(
            locator=ForgotPasswordPageLocators.FIELD_PASSWORD).send_keys(TestForgotPasswordData.password)

    @allure.step("Найти в поле 'Пароль' значок 'Глаз' кликнуть по нему")
    def find_element_eye_and_click(self):
        self.find_element(locator=ForgotPasswordPageLocators.EYE_ACTIVE).click()



