import allure
from pages.login_page import LoginPageHelper


class TestPersonalCabinet:
    @allure.title('Проверить, переход по клику на «Личный кабинет»')
    @allure.description("Логинимся готовым пользователем, кликаем по кнопке 'Личный кабинет' проверяем что на"
                        "странице есть элемент текс 'Профиль'")
    def test_click_on_personal_account(self, driver, log_in):
        login_page = LoginPageHelper(driver)
        login_page.click_on_the_personal_account_button()
        assert login_page.find_element_profile_in_personal_cabinet(), \
            "Не найден элемент текст 'Профиль' в личном кабинете"

    @allure.title('Проверить, переход в раздел «История заказов»')
    @allure.description("Логинимся готовым пользователем, кликаем по кнопке 'Личный кабинет'"
                        "кликаем по тексту 'История заказов'")
    def test_go_to_the_order_history_section(self, driver, log_in):
        login_page = LoginPageHelper(driver)
        login_page.click_on_the_personal_account_button()
        login_page.click_on_the_text_history_section()
        assert login_page.find_active_element_history_orders(), \
            "Не найден выбранный элемент текст 'История заказов' в личном кабинете"

    @allure.title('Проверить, выход из аккаунта')
    @allure.description("Логинимся готовым пользователем, переходим в личный кабинет, кликаем по кнопке выход"
                        "проверяем что на странице нет элемента 'Выход'")
    def test_exit_of_account(self, driver, log_in):
        login_page = LoginPageHelper(driver)
        login_page.click_on_the_personal_account_button()
        login_page.click_on_the_text_exit_section()
        assert login_page.find_element_exit(), "Не найден выбранный элемент текст 'Выход' на странице логина"
