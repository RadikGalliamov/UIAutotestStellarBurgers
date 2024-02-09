import allure

from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPageHelper


class PersonalCabinetPageHelper(MainPageHelper):
    @allure.step("Клик по разделу 'История'")
    def click_on_the_text_history_section(self):
        self.wait_and_click(locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT)

    @allure.step("Клик по разделу 'Выход'")
    def click_on_the_text_exit_section(self):
        self.wait_and_click(locator=PersonalCabinetPageLocators.EXIT_TEXT)
