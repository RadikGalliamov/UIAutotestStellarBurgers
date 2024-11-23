import allure
from selenium.webdriver.common.by import By
from data import TestDataUrl, TestLoginPageData
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.main_page import MainPageHelper


class LoginPageHelper(MainPageHelper):
    """
    LoginPageLocators
    """
    ENTER_TEXT = (By.XPATH, ".//h2[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")  # Поле 'Email'
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")  # Поле 'Пароль'
    ENTER = (By.XPATH, ".//button[text()='Войти']")  # Кнопка 'Войти'
    TEXT_RECOVER_PASSWORD = (By.XPATH, ".//a[@class='Auth_link__1fOlj'][text()='Восстановить пароль']")

    """
    PersonalCabinetPageLocators
    """
    """
    - HEADER
    """
    BUTTON_ORDER_HEADER = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")

    """
    - MAIN AREA
    """
    BUTTON_ORDER_MAIN_AREA = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    PROFILE_TEXT = (By.XPATH, "//a[text()='Профиль']")
    HISTORY_OF_ORDERS_TEXT = (By.XPATH, "//a[text()='История заказов']")
    HISTORY_OF_ORDERS_TEXT_ACTIVE = (
        By.XPATH,
        "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='История заказов']")
    EXIT_TEXT = (By.XPATH, ".//button[@type='button' and text()='Выход']")
    """
    ForgotPasswordPageLocators
    """
    TEXT_PASSWORD_RECOVERY = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Восстановление пароля']")

    def __init__(self, driver):
        super().__init__(driver)
        # self.email_field = LoginPageLocators.EMAIL_FIELD
        # self.password_field = LoginPageLocators.PASSWORD_FIELD
        # self.enter_button = LoginPageLocators.ENTER

    @allure.step("Авторизация")
    def login(self):
        self._open(TestDataUrl.LOGIN_PAGE_URL)
        self._find_element(self.EMAIL_FIELD).send_keys(TestLoginPageData.email)
        self._find_element(self.PASSWORD_FIELD).send_keys(TestLoginPageData.password)
        self._find_element(self.ENTER).click()

    @allure.step("Клик по тексту 'Восстановить пароль'")
    def click_on_the_text_recover_password(self):
        self._wait_and_click(locator=self.TEXT_RECOVER_PASSWORD)

    @allure.step("Клик по тексту 'Личный кабинет'")
    def click_on_the_text_personal_cabinet(self):
        self._find_element(self.PERSONAL_CABINET_TEXT, 30).click()

    @allure.step("Найти текст 'Профиль'")
    def find_text_profile(self):
        self._find_element(self.PROFILE_TEXT)

    @allure.step("Клик по разделу 'История заказов'")
    def click_on_the_text_history_section(self):
        self._wait_and_click(locator=self.HISTORY_OF_ORDERS_TEXT)

    @allure.step("Клик по разделу 'Выход'")
    def click_on_the_text_exit_section(self):
        self._wait_and_click(locator=self.EXIT_TEXT)

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

    # метод использует чужой локатор, переделать метод вызывать из другого класса
    @allure.step("Найти элемент - текст 'Восстановление пароля'")
    def find_element_recovery_password(self):
        return self._find_element(locator=self.TEXT_PASSWORD_RECOVERY)

    @allure.step("Найти элемент текст 'Профиль' в личном кабинете")
    def find_element_profile_in_personal_cabinet(self):
        return self._find_element(locator=self.PROFILE_TEXT)

    @allure.step("Найти активный элемент текст 'История заказов'")
    def find_active_element_history_orders(self):
        return self._find_element(locator=self.HISTORY_OF_ORDERS_TEXT_ACTIVE)

    @allure.step("Найти элемент текст 'Выход'")
    def find_element_exit(self):
        return self._find_element(locator=self.ENTER_TEXT)
