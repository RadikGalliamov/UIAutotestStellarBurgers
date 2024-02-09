import allure

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage
from data import TestLoginPageData
from pages.main_page import MainPageHelper


class LoginPageHelper(MainPageHelper):
    @allure.step("Клик по тексту 'Восстановить пароль'")
    def click_on_the_text_recover_password(self):
        self.wait_and_click(locator=LoginPageLocators.TEXT_RECOVER_PASSWORD)

    @allure.step("Клик по тексту 'Личный кабинет'")
    def click_on_the_text_personal_cabinet(self):
        self.find_element(MainPageLocators.PERSONAL_CABINET_TEXT, 30).click()

    @allure.step("Найти текст 'Профиль'")
    def find_text_profile(self):
        self.find_element(PersonalCabinetPageLocators.PROFILE_TEXT)

    @allure.step("Найти текст 'Kjuby'")
    def log_in(self):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(TestLoginPageData.email)
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(TestLoginPageData.password)
        self.find_element(LoginPageLocators.ENTER).click()

