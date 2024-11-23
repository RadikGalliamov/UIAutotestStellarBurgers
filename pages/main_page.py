import allure
from data import TestMainPageData
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPageHelper(BasePage):
    """
    - HEADER
    """
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка Конструктор
    PERSONAL_CABINET_TEXT = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")  # Кнопка Лента заказов
    """
    - MAIN AREA
    """
    ASSEMBLE_THE_BURGER_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Текст 'Соберите бургер'
    ORDER_FEED_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")  # Текст 'Лента заказов'
    INGREDIENT_BUN = (
        By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # Ингредиент Флюоресцентная булка R2-D3
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")  # Текст 'Детали ингредиента'
    INGREDIENT_DETAILS_CLOSE = (
        By.XPATH, "(.//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    # Закрыть всплывающее окно 'Детали ингредиента'
    ORDER_AREA = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # Область заказа
    BUN_INGREDIENT_COUNTER = (
        By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[starts-with(@class,'counter')]")
    # Счетчик ингредиента булка
    MAKE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка 'Оформить заказ'
    MODAL_WINDOW_ID_ORDER = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")
    # модальное окно 'Идентификатор заказа'
    ANY_ORDER_IN_ORDER_FEED = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    # один любой заказ из списка заказов в 'Ленте заказов'
    MODAL_WINDOW_ORDER_IN_ORDER_FEED = (By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    # Модальное окно заказа в 'Ленте заказов'
    ID_ORDER_IN_MODAL_WINDOW = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    # номер заказа в модальном окне 'Идентификатор заказа'
    CLOSE_ID_ORDER_MODAL_WINDOW = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # крестик для закрытия модального окна 'Идентификатор заказа'
    ALL_ORDERS_IN_HISTORY_ORDERS = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # все заказы пользователя в разделе 'История заказов'
    ALL_ORDERS_IN_ORDER_FEED = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # все заказы пользователя в разделе 'Лента заказов'
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")
    # счетчик выполнено за все время заказов в 'Ленте Заказов'
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")
    # счетчик 'Выполнено за сегодня' заказов в 'Ленте Заказов'
    IN_WORK_FEED_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
    # id заказа в статусе 'В работе' в разделе 'Ленте Заказов'
    """
    - FOOTER
    """
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_on_the_login_to_account_button(self):
        self._wait_and_click(locator=self.BUTTON_LOGIN_TO_ACCOUNT)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_the_personal_account_button(self):
        self._wait_for_clickable(self.PERSONAL_CABINET_TEXT).click()

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_the_constructor_button(self):
        self._wait_and_click(locator=self.CONSTRUCTOR_BUTTON)

    @allure.step("Найти текст 'Соберите бургер'")
    def find_text_assemble_the_burger(self):
        return self._find_element(locator=self.ASSEMBLE_THE_BURGER_TEXT)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_the_order_feed(self):
        self._wait_and_click(locator=self.ORDER_FEED_BUTTON)

    @allure.step("Найти текст 'Лента заказов'")
    def find_text_the_order_feed(self):
        return self._find_element(locator=self.ORDER_FEED_TEXT)

    @allure.step("Клик по ингредиенту 'Флюоресцентная булка R2-D3'")
    def find_and_click_on_the_bun(self):
        self._wait_for_clickable(MainPageLocators.INGREDIENT_BUN).click()

    @allure.step("Найти текст 'Детали ингредиента' всплывающего окна 'Детали ингредиента'")
    def find_text_the_ingredient_details(self):
        return self._wait_for_visibility(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Не найден текст 'Детали ингредиента' всплывающего окна 'Детали ингредиента'")
    def not_find_text_the_order_feed(self):
        return self._not_find_element(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Найти элемент крестик и закрыть всплывающее окна 'Детали ингредиента'")
    def find_and_click_the_element_close_pop_up_ingredient_details(self):
        return self._wait_for_clickable(locator=MainPageLocators.INGREDIENT_DETAILS_CLOSE).click()

    @allure.step("Перемещение элемента в заказ")
    def drag_item_to_order(self):
        element = self._find_element(locator=self.INGREDIENT_BUN)
        location = self._find_element(locator=self.ORDER_AREA)
        self._drag_and_drop_element(element_to_drag=element, target_location=location)

    @allure.step("Количество элементов в счетчике булки 'Флюоресцентная булка R2-D3'")
    def number_of_elements_in_the_roll_counter_fluorescent_roll_r2_d3(self):
        return self._find_element(locator=self.BUN_INGREDIENT_COUNTER).text

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_on_the_place_an_order_button(self):
        return self._wait_and_click(locator=self.MAKE_AN_ORDER_BUTTON)

    @allure.step("Появилось модальное окно 'Идентификатор заказа'")
    def the_order_id_modal_windows_appears(self):
        return self._find_element(locator=self.MODAL_WINDOW_ID_ORDER)

    @allure.step("Кликнуть по одному любому заказу в разделе 'Лента заказов'")
    def click_on_any_one_order_in_the_order_feed_section(self):
        return self._find_element(locator=self.ANY_ORDER_IN_ORDER_FEED).click()

    @allure.step("Появилось модальное окно 'Данные о заказа' в разделе 'Лента заказов'")
    def appeared_the_order_id_modal_windows_data_of_order_in_order_feed(self):
        return self._find_element(locator=self.MODAL_WINDOW_ORDER_IN_ORDER_FEED)

    @allure.step("Ожидаем исчезновения id 99999 в модальном окне 'Идентификатор заказа'")
    def disappearance_of_invalid_id_in_the_order_id_modal_window(self):
        self._is_disappeared(
            locator=self.ID_ORDER_IN_MODAL_WINDOW, text=TestMainPageData.text_in_id_modal_windows)

    @allure.step("Получить ID заказа в модальном окне 'Идентификатор заказа'")
    def the_order_id_modal_windows_data_of_order_in_order_feed(self):
        return self._find_element(locator=self.ID_ORDER_IN_MODAL_WINDOW).text

    @allure.step("Закрыть модальное окно 'Идентификатор заказа'")
    def close_modal_window_id_order(self):
        return self._wait_for_clickable(locator=self.CLOSE_ID_ORDER_MODAL_WINDOW).click()

    @allure.step("Собрать все id заказов из раздела 'История заказов'")
    def collect_all_order_ids_from_order_history_section(self):
        elements = self._find_elements(locator=self.ALL_ORDERS_IN_HISTORY_ORDERS)
        text_values = [element.text.strip() for element in elements]
        return text_values

    @allure.step("Собрать все id заказов из раздела 'Лента заказов'")
    def collect_all_order_ids_from_order_feed_section(self):
        elements = self._find_elements(locator=self.ALL_ORDERS_IN_ORDER_FEED)
        text_values = [element.text.strip() for element in elements]
        return text_values

    @allure.step("Получить количество заказов 'Выполнено за все время' в разделе 'Лента заказов'")
    def get_the_number_of_orders_for_all_time_in_the_order_feed_section(self):
        return self._find_element(locator=self.COUNTER_COMPLETED_FOR_ALL_TIME).text

    @allure.step("Получить количество заказов 'Выполнено за сегодня' в разделе 'Лента заказов'")
    def get_the_number_of_orders_for_today_in_the_order_feed_section(self):
        return self._find_element(locator=self.COUNTER_COMPLETED_TODAY).text

    @allure.step("Получить ID заказа в статусе 'В работе' в разделе 'Лента заказов'")
    def get_order_id_in_status_in_order_feed_section(self):
        self._is_disappeared(locator=self.IN_WORK_FEED_ORDER, text=TestMainPageData.text)
        return self._find_element(locator=self.IN_WORK_FEED_ORDER).text.strip()

    @allure.step('Создать заказ и сохранить номер заказа')
    def create_order_and_return_order(self):
        self.drag_item_to_order()
        self.click_on_the_place_an_order_button()
        self.disappearance_of_invalid_id_in_the_order_id_modal_window()
        order = self.the_order_id_modal_windows_data_of_order_in_order_feed()
        self.close_modal_window_id_order()
        return order

    @allure.step('Создать один заказ и сохранить количество заказа раздела "Выполнено за сегодня"')
    def create_order_and_save_order_numbers_in_completed_today_section(self):
        self.drag_item_to_order()
        self.click_on_the_place_an_order_button()
        self.disappearance_of_invalid_id_in_the_order_id_modal_window()
        self.close_modal_window_id_order()
        self.click_on_the_order_feed()
        orders_for_today = self.get_the_number_of_orders_for_today_in_the_order_feed_section()
        return orders_for_today

    @allure.step('Создать один заказ и сохранить количество заказа раздела "Выполнено за все время"')
    def create_order_and_save_order_numbers_in_completed_for_all_time_section(self):
        self.drag_item_to_order()
        self.click_on_the_place_an_order_button()
        self.disappearance_of_invalid_id_in_the_order_id_modal_window()
        self.close_modal_window_id_order()
        self.click_on_the_order_feed()
        orders_for_all_time = self.get_the_number_of_orders_for_all_time_in_the_order_feed_section()
        return orders_for_all_time
