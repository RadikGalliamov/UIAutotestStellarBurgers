import allure
from locators.login_page_locators import LoginPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.login_page import LoginPageHelper


class TestPersonalCabinet:
    @allure.title('Проверить, переход по клику на «Личный кабинет»')
    @allure.description("Логинимся готовым пользователем, кликаем по кнопке 'Личный кабинет' проверяем что на"
                        "странице есть элемент текс 'Профиль'")
    def test_click_on_personal_account(self, log_in):
        login_page = LoginPageHelper(driver=log_in)
        login_page.click_on_the_personal_account_button()
        assert login_page.find_element(
            locator=PersonalCabinetPageLocators.PROFILE_TEXT), "Не найден элемент текст 'Профиль' в личном кабинете"

    @allure.title('Проверить, переход в раздел «История заказов»')
    @allure.description("Логинимся готовым пользователем, кликаем по кнопке 'Личный кабинет'"
                        "кликаем по тексту 'История заказов'")
    def test_go_to_the_order_history_section(self, log_in):
        login_page = LoginPageHelper(driver=log_in)
        login_page.click_on_the_personal_account_button()
        login_page.click_on_the_text_history_section()
        assert login_page.find_element(
            locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT_ACTIVE), "Не найден выбранный элемент текст 'История заказов' в личном кабинете"

    @allure.title('Проверить, выход из аккаунта')
    @allure.description("Логинимся готовым пользователем, переходим в личный кабинет, кликаем по кнопке выход"
                        "проверяем что на странице нет элемента 'Выход'")
    def test_exit_of_account(self, log_in):
        login_page = LoginPageHelper(driver=log_in)
        login_page.click_on_the_personal_account_button()
        login_page.click_on_the_text_exit_section()
        assert login_page.find_element(
            locator=LoginPageLocators.ENTER_TEXT), "Не найден выбранный элемент текст 'Выход' на странице логина"
