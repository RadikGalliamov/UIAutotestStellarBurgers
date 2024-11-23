import allure
from data import TestDataUrl, TestForgotRecoveryData
from pages.login_page import LoginPageHelper
from pages.forgot_password_page import ForgotPasswordPageHelper


class TestPasswordRecovery:
    @allure.title(
        'Проверить, что клик по кнопке «Восстановить пароль» переводит на страницу запроса восстановления пароля')
    @allure.description("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_the_password_recovery_page_by_clicking_the_recover_password_button(self, driver):
        login_page = LoginPageHelper(driver=driver)
        login_page._open(url=TestDataUrl.LOGIN_PAGE_URL)
        login_page.click_on_the_text_recover_password()
        assert login_page.find_element_recovery_password()
        "Не найден элемент - текст 'Восстановление пароля' на странице восстановления пароля"

    @allure.title(
        "Проверка, что ввод почты и клик по кнопке 'Восстановить' введет на страницу восстановления пароля")
    @allure.description(
        "На странице восстановления пароля вводим email и переходим на страницу восстановление пароля"
        "с получением кода")
    def test_enter_mail_click_restore_button_go_to_restore_page(self, driver):
        recover_password_page = ForgotPasswordPageHelper(driver=driver)
        recover_password_page._open(url=TestDataUrl.PASSWORD_RECOVERY_PAGE_URL)
        recover_password_page.find_and_enter_field_mail_address(email=TestForgotRecoveryData.email)
        recover_password_page.find_and_click_recovery_button()
        assert recover_password_page.find_field_enter_pass_from_mail(), "Не найдено поле 'Введите код из письма'"

    @allure.title(
        "Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description(
        "На странице восстановления пароля клик по знакчку 'глаз' скрывает/показывает введенный в поле пароль")
    def test_click_on_the_eye_makes_field_active(self, driver):
        recover_password_page = ForgotPasswordPageHelper(driver=driver)
        recover_password_page._open(url=TestDataUrl.PASSWORD_RECOVERY_PAGE_URL)
        recover_password_page.find_and_enter_field_mail_address(email=TestForgotRecoveryData.email)
        recover_password_page.find_and_click_recovery_button()
        recover_password_page.find_click_and_input_password_in_field_password()
        recover_password_page.find_element_eye_and_click()
        assert recover_password_page.find_field_active_field_password, "Не найдено активное поле 'Пароль'"
