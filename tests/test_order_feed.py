import allure
from data import TestDataUrl
from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper


class TestOrderFeedPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description(
        "Переходим в раздел Лента заказов, кликаем любой заказ, видим что появилось модальное окно с данными о заказе")
    def test_click_on_the_order_opens_a_window_with_order_details(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.LOGIN_PAGE_URL)
        page.click_on_the_order_feed()
        page.click_on_any_one_order_in_the_order_feed_section()
        assert page.the_order_id_modal_windows_appears(), "Не появилось модальное окно 'Данные о заказе'"

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description(
        "Залогинится пользователем с заказами, собрать список заказов из Истории заказов и сверить каждое значение списка со списком из раздела Лента заказов")
    def test_orders_from_the_order_history_section_are_displayed_on_the_order_feed_page(self, log_in):
        page = LoginPageHelper(log_in)
        page.click_on_the_text_personal_cabinet()
        page.click_on_the_text_history_section()
        id_orders_history = page.collect_all_order_ids_from_order_history_section()
        page.click_on_the_order_feed()
        id_orders_feed = page.collect_all_order_ids_from_order_feed_section()
        assert page.check_lists_history_orders_and_order_feed(list1=id_orders_history, list2=id_orders_feed), "Заказы пользователя из 'Истории заказов' не отображаються в 'Ленте заказов'"

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description(
        "Логинимся готовым пользователем, сохраняем текущее количество заказов в разделе Выполнено за всё время, создаем один заказ, снова сохраняем количество заказов в разделе Выполнено за всё время и сравниваем сохраненные значение до и после заказа")
    def test_when_new_order_is_created_the_completed_counter_for_all_time_increases(self, log_in):
        page = MainPageHelper(log_in)
        page.click_on_the_order_feed()
        counter_orders = page.get_the_number_of_orders_for_all_time_in_the_order_feed_section()
        page.open_url(TestDataUrl.MAIN_URL)
        page.drag_item_to_order()
        page.click_on_the_place_an_order_button()
        page.disappearance_of_invalid_id_in_the_order_id_modal_window()
        page.close_modal_window_id_order()
        page.click_on_the_order_feed()
        counter_orders_udp = page.get_the_number_of_orders_for_all_time_in_the_order_feed_section()
        assert counter_orders != counter_orders_udp, "Cчётчик 'Выполнено за всё время' в разделе Лента заказов не увеличивается, после оформления нового заказа"

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description(
        'Логинимся готовым пользователем, сохраняем текущее количество заказов в разделе "Выполнено за сегодня"'
        '"Ленты заказов", создаем один заказ, сохраняем количество заказов в разделе "Выполнено за сегодня"'
        '"Ленты заказов" и сравниваем сохраненные значение до и после заказа')
    def test_when_new_order_is_created_the_completed_counter_for_today_increases(self, log_in):
        page = MainPageHelper(log_in)
        page.click_on_the_order_feed()
        counter_orders = page.get_the_number_of_orders_for_today_in_the_order_feed_section()
        page.open_url(TestDataUrl.MAIN_URL)
        page.drag_item_to_order()
        page.click_on_the_place_an_order_button()
        page.disappearance_of_invalid_id_in_the_order_id_modal_window()
        page.close_modal_window_id_order()
        page.click_on_the_order_feed()
        counter_orders_udp = page.get_the_number_of_orders_for_today_in_the_order_feed_section()
        assert counter_orders != counter_orders_udp, "Cчётчик 'Выполнено за сегодня' в разделе 'Лента заказов' не увеличивается, после оформления нового заказа"

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Логинимся готовым пользователем, создать один заказ, получить id заказа'
                        'сравнить что полученный id заказа появился в "Ленте заказов"'
                        'в статусе "В работе"')
    def test_after_placing_an_order_its_number_appears_in_the_in_progress_section(self, log_in):
        page = MainPageHelper(log_in)
        page.drag_item_to_order()
        page.click_on_the_place_an_order_button()
        page.disappearance_of_invalid_id_in_the_order_id_modal_window()
        id_order = page.the_order_id_modal_windows_data_of_order_in_order_feed()
        page.close_modal_window_id_order()
        page.click_on_the_order_feed()
        assert page.get_the_order_id_in_the_in_progress_status_in_the_order_feed_section()[1:] == id_order, "id заказа отсутствует в в статусе В работе раздела Лента заказов "
