import allure
from data import TestDataUrl
from pages.main_page import MainPageHelper


class TestMainPage:
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description("Со страницы логина кликаем на текст конструктор и попадаем на страницу конструктора")
    def test_click_on_constructor(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.LOGIN_PAGE_URL)
        page.click_on_the_constructor_button()
        assert page.find_text_assemble_the_burger(), "Не найден элемент текст 'Собери бургер'"

    @allure.title('Переход по клику на «Лента заказов»')
    @allure.description("Со страницы логина кликаем на текст Лента заказов и попадаем на страницу Лента заказов")
    def test_click_on_order_feed(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.LOGIN_PAGE_URL)
        page.click_on_the_order_feed()
        assert page.find_text_the_order_feed(), "Не найден элемент текст 'Лента заказов'"

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description("Кликаем на элемент булка, в сплывающем окне находим текст 'Детали ингредиента'")
    def test_click_on_ingredient_pop_up_will_appear_with_details(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.MAIN_URL)
        page.find_and_click_on_the_bun()
        assert page.find_text_the_ingredient_details(), "Не найден элемент текст 'Детали ингредиента' всплавающего окна 'Детали ингредиента'"

    @allure.title('Всплывающее окно закрывается кликом по элементу крестик')
    @allure.description(
        "Кликаем на элемент булка, всплывающем окне находим текст 'Детали ингредиента' закрываем окно через крестик, всплавающее окно должно закрытся")
    def test_the_pop_up_window_is_closed_by_clicking_on_the_cross_element(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.MAIN_URL)
        page.find_and_click_on_the_bun()
        page.find_and_click_the_element_close_pop_up_ingredient_details()
        assert page.not_find_text_the_order_feed(), "Найден элемент текст 'Детали ингредиента' всплавающего окна 'Детали ингредиента'"

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description(
        "Кликаем на элемент булка, перемещаем элемент булка в область заказа, проверяем счетчик в области элемента 'Флюоресцентная булка R2-D3'")
    def test_when_add_an_ingredient_to_an_order_the_counter_for_that_ingredient_increases(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.MAIN_URL)
        page.drag_item_to_order()
        assert page.number_of_elements_in_the_roll_counter_fluorescent_roll_r2_d3() != "0"

    @allure.title('Аутентифицированный  пользователь может оформить заказ')
    @allure.description(
        "Аунтифицируемся пользователем, перетаскиваем элемент булка в область добавления заказа, кликаем кнопку 'Оформить заказ', получаем модальное окно 'Идентификатор заказа'")
    def test_an_authenticated_user_can_place_an_order(self, log_in):
        page = MainPageHelper(log_in)
        page.drag_item_to_order()
        page.click_on_the_place_an_order_button()
        assert page.the_order_id_modal_windows_appears(), "Не появилось модальное окно 'Идентификатор заказа'"
