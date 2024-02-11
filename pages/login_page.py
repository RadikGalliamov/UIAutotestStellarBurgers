import allure

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
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
