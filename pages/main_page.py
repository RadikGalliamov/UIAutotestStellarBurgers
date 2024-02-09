import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPageHelper(BasePage):

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_on_the_login_to_account_button(self):
        self.wait_and_click(locator=MainPageLocators.BUTTON_LOGIN_TO_ACCOUNT)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_the_personal_account_button(self):
        self.wait_for_clickable(MainPageLocators.PERSONAL_CABINET_TEXT).click()
