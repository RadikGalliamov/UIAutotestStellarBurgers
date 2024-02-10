import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


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
    def find_text_the_order_feed(self):
        return self.wait_for_visibility(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Не найден текст 'Детали ингредиента' всплывающего окна 'Детали ингредиента'")
    def not_find_text_the_order_feed(self):
        return self.not_find_element(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Найти элемент крестик для закрытия всплывающего окна 'Детали ингредиента'")
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
        return self.find_element(locator=MainPageLocators.MAKE_AN_ORDER_BUTTON).click()

    @allure.step("Появилось модальное окно 'Идентификатор заказа'")
    def the_order_id_modal_windows_appears(self):
        return self.find_element(locator=MainPageLocators.MODAL_WINDOW_ID_ORDER)