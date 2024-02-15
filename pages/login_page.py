import allure

from data import TestDataUrl, TestLoginPageData
from locators.forgot_password_locators import ForgotPasswordPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.main_page import MainPageHelper
from locators.login_page_locators import LoginPageLocators


class LoginPageHelper(MainPageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = LoginPageLocators.EMAIL_FIELD
        self.password_field = LoginPageLocators.PASSWORD_FIELD
        self.enter_button = LoginPageLocators.ENTER

    @allure.step("Авторизация")
    def login(self):
        self.open_url(TestDataUrl.LOGIN_PAGE_URL)
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(TestLoginPageData.email)
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(TestLoginPageData.password)
        self.find_element(LoginPageLocators.ENTER).click()

    @allure.step("Клик по тексту 'Восстановить пароль'")
    def click_on_the_text_recover_password(self):
        self.wait_and_click(locator=LoginPageLocators.TEXT_RECOVER_PASSWORD)

    @allure.step("Клик по тексту 'Личный кабинет'")
    def click_on_the_text_personal_cabinet(self):
        self.find_element(MainPageLocators.PERSONAL_CABINET_TEXT, 30).click()

    @allure.step("Найти текст 'Профиль'")
    def find_text_profile(self):
        self.find_element(PersonalCabinetPageLocators.PROFILE_TEXT)

    @allure.step("Клик по разделу 'История заказов'")
    def click_on_the_text_history_section(self):
        self.wait_and_click(locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT)

    @allure.step("Клик по разделу 'Выход'")
    def click_on_the_text_exit_section(self):
        self.wait_and_click(locator=PersonalCabinetPageLocators.EXIT_TEXT)

    @allure.step("Проверить список заказов из 'Истории заказов' пользователя в списке 'Ленты заказов'")
    def check_lists_history_orders_and_order_feed(self, list1, list2):
        for value1 in list1:
            found = False
            for value2 in list2:
                if value1 == value2:
                    found = True
                    break
            if not found:
                return False
        return True

    @allure.step("Найти элемент - текст 'Восстановление пароля'")
    def find_element_recovery_password(self):
        return self.find_element(locator=ForgotPasswordPageLocators.TEXT_PASSWORD_RECOVERY)

    @allure.step("Найти элемент текст 'Профиль' в личном кабинете")
    def find_element_profile_in_personal_cabinet(self):
        return self.find_element(locator=PersonalCabinetPageLocators.PROFILE_TEXT)

    @allure.step("Найти активный элемент текст 'История заказов'")
    def find_active_element_history_orders(self):
        return self.find_element(locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT_ACTIVE)

    @allure.step("Найти элемент текст 'Выход'")
    def find_element_exit(self):
        return self.find_element(locator=LoginPageLocators.ENTER_TEXT)
