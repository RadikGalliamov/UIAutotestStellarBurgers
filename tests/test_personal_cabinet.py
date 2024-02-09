import allure
from locators.login_page_locators import LoginPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper
from data import TestDataUrl
from pages.personal_cabinet_page import PersonalCabinetPageHelper


class TestPersonalCabinet:
    @allure.title(
        'Проверить, переход по клику на «Личный кабинет»')
    @allure.description("")
    def test_click_on_personal_account(self, driver):
        page = MainPageHelper(driver=driver, url=TestDataUrl.MAIN_URL)
        page.open()
        page.click_on_the_login_to_account_button()
        login_page = LoginPageHelper(driver=driver, url=driver.current_url)
        login_page.log_in()
        page = MainPageHelper(driver=driver, url=driver.current_url)
        page.click_on_the_personal_account_button()
        assert page.find_element(
            locator=PersonalCabinetPageLocators.PROFILE_TEXT), "Не найден элемент текст 'Профиль' в личном кабинете"

    @allure.title(
        'Проверить, переход в раздел «История заказов»')
    @allure.description("")
    def test_go_to_the_order_history_section(self, driver):
        page = MainPageHelper(driver=driver, url=TestDataUrl.MAIN_URL)
        page.open()
        page.click_on_the_login_to_account_button()
        login_page = LoginPageHelper(driver=driver, url=driver.current_url)
        login_page.log_in()
        page = MainPageHelper(driver=driver, url=driver.current_url)
        page.click_on_the_personal_account_button()
        personal_cabinet_page = PersonalCabinetPageHelper(driver=driver, url=driver.current_url)
        personal_cabinet_page.click_on_the_text_history_section()
        assert personal_cabinet_page.find_element(
            locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT_ACTIVE), "Не найден выбранный элемент текст 'История заказов' в личном кабинете"

    @allure.title(
        'Проверить, выход из аккаунта')
    @allure.description("")
    def test_exit_of_account(self, driver):
        page = MainPageHelper(driver=driver, url=TestDataUrl.MAIN_URL)
        page.open()
        page.click_on_the_login_to_account_button()
        login_page = LoginPageHelper(driver=driver, url=driver.current_url)
        login_page.log_in()
        page = MainPageHelper(driver=driver, url=driver.current_url)
        page.click_on_the_personal_account_button()
        personal_cabinet_page = PersonalCabinetPageHelper(driver=driver, url=driver.current_url)
        personal_cabinet_page.click_on_the_text_exit_section()
        assert personal_cabinet_page.find_element(
            locator=LoginPageLocators.ENTER_TEXT), "Не найден выбранный элемент текст 'Вход' на странице логина"
