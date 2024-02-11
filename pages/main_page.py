import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from data import TestMainPageData
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MainPageHelper(BasePage):

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_on_the_login_to_account_button(self):
        self.wait_and_click(locator=MainPageLocators.BUTTON_LOGIN_TO_ACCOUNT)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_the_personal_account_button(self):
        self.wait_for_clickable(MainPageLocators.PERSONAL_CABINET_TEXT).click()

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_the_constructor_button(self):
        self.wait_and_click(locator=MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Найти текст 'Соберите бургер'")
    def find_text_assemble_the_burger(self):
        return self.find_element(locator=MainPageLocators.ASSEMBLE_THE_BURGER_TEXT)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_the_order_feed(self):
        self.wait_and_click(locator=MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Найти текст 'Лента заказов'")
    def find_text_the_order_feed(self):
        return self.find_element(locator=MainPageLocators.ORDER_FEED_TEXT)

    @allure.step("Клик по ингредиенту 'Флюоресцентная булка R2-D3'")
    def find_and_click_on_the_bun(self):
        self.wait_for_clickable(MainPageLocators.INGREDIENT_BUN).click()

    @allure.step("Найти текст 'Детали ингредиента' всплывающего окна 'Детали ингредиента'")
    def find_text_the_ingredient_details(self):
        return self.wait_for_visibility(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Не найден текст 'Детали ингредиента' всплывающего окна 'Детали ингредиента'")
    def not_find_text_the_order_feed(self):
        return self.not_find_element(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Найти элемент крестик и закрыть всплывающее окна 'Детали ингредиента'")
    def find_and_click_the_element_close_pop_up_ingredient_details(self):
        return self.wait_for_clickable(locator=MainPageLocators.INGREDIENT_DETAILS_CLOSE).click()

    @allure.step("Перемещение элемента в заказ")
    def drag_item_to_order(self):
        element = self.find_element(locator=MainPageLocators.INGREDIENT_BUN)
        location = self.find_element(locator=MainPageLocators.ORDER_AREA)
        self.drag_and_drop_element(element_to_drag=element, target_location=location)

    @allure.step("Количество элементов в счетчике булки 'Флюоресцентная булка R2-D3'")
    def number_of_elements_in_the_roll_counter_fluorescent_roll_r2_d3(self):
        return self.find_element(locator=MainPageLocators.BUN_INGREDIENT_COUNTER).text

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_on_the_place_an_order_button(self):
        return self.wait_and_click(locator=MainPageLocators.MAKE_AN_ORDER_BUTTON)

    @allure.step("Появилось модальное окно 'Идентификатор заказа'")
    def the_order_id_modal_windows_appears(self):
        return self.find_element(locator=MainPageLocators.MODAL_WINDOW_ID_ORDER)

    @allure.step("Кликнуть по одному любому заказу в разделе 'Лента заказов'")
    def click_on_any_one_order_in_the_order_feed_section(self):
        return self.find_element(locator=MainPageLocators.ANY_ORDER_IN_ORDER_FEED).click()

    @allure.step("Появилось модальное окно 'Данные о заказа' в разделе 'Лента заказов'")
    def appeared_the_order_id_modal_windows_data_of_order_in_order_feed(self):
        return self.find_element(locator=MainPageLocators.MODAL_WINDOW_ORDER_IN_ORDER_FEED)

    @allure.step("Ожидаем исчезновения id 99999 в модальном окне 'Идентификатор заказа'")
    def disappearance_of_invalid_id_in_the_order_id_modal_window(self):
        self.is_disappeared(
            locator=MainPageLocators.ID_ORDER_IN_MODAL_WINDOW,
            text_in_element=TestMainPageData.text_in_id_modal_windows)

    @allure.step("Получить ID заказа в модальном окне 'Идентификатор заказа'")
    def the_order_id_modal_windows_data_of_order_in_order_feed(self):
        time.sleep(2)
        return self.find_element(locator=MainPageLocators.ID_ORDER_IN_MODAL_WINDOW).text

    @allure.step("Закрыть модальное окно 'Идентификатор заказа'")
    def close_modal_window_id_order(self):
        return self.wait_for_clickable(locator=MainPageLocators.CLOSE_ID_ORDER_MODAL_WINDOW).click()

    @allure.step("Собрать все id заказов из раздела 'История заказов'")
    def collect_all_order_ids_from_order_history_section(self):
        elements = self.find_elements(MainPageLocators.ALL_ORDERS_IN_HISTORY_ORDERS)
        text_values = [element.text.strip() for element in elements]
        return text_values

    @allure.step("Собрать все id заказов из раздела 'Лента заказов'")
    def collect_all_order_ids_from_order_feed_section(self):
        elements = self.find_elements(MainPageLocators.ALL_ORDERS_IN_ORDER_FEED)
        text_values = [element.text.strip() for element in elements]
        return text_values

    @allure.step("Получить количество заказов 'Выполнено за все время' в разделе 'Лента заказов'")
    def get_the_number_of_orders_for_all_time_in_the_order_feed_section(self):
        return self.find_element(locator=MainPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text

    @allure.step("Получить количество заказов 'Выполнено за сегодня' в разделе 'Лента заказов'")
    def get_the_number_of_orders_for_today_in_the_order_feed_section(self):
        return self.find_element(locator=MainPageLocators.COUNTER_COMPLETED_TODAY).text

    @allure.step("Получить ID заказа в статусе 'В работе' в разделе 'Лента заказов'")
    def get_the_order_id_in_the_in_progress_status_in_the_order_feed_section(self):
        time.sleep(2)
        # Ожидаем, пока текст "Все текущие заказы готовы!" исчезнет из элемента
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(MainPageLocators.IN_WORK_FEED_ORDER, 'Все текущие заказы готовы!')
        )
        # Возвращаем текст элемента после исчезновения "Все текущие заказы готовы!"
        return self.find_element(locator=MainPageLocators.IN_WORK_FEED_ORDER).text.strip()
