import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    @allure.step('Создаем объекта класса BasePage')
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент с ожиданием")
    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time) \
            .until(EC.presence_of_element_located(locator),
                   message=f"Не найден элемент = {locator}")

    @allure.step("Ожидание и клик по элементу")
    def wait_and_click(self, locator, wait_time=10):
        element = self.find_element(locator, wait_time)
        element.click()

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}")
        return element

    @allure.step("Ожидание кликабельного элемента")
    def wait_for_clickable(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}"
        )
        WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не стал кликабельным: {locator}"
        )
        return element

    @allure.step('Ожидание отсутствия локатора')
    def not_find_element(self, locator, time=30):
        return WebDriverWait(
            self.driver, time
        ).until(
            expected_conditions.none_of(
                expected_conditions.visibility_of_element_located(locator)
            ),
            message=f'Элемент найден'
        )

    @allure.step("Переместить элемент на другое место на странице")
    def drag_and_drop_element(self, element_to_drag, target_location):
        action_chains = ActionChains(self.driver)
        # Выполнение действия перетаскивания и бросания элемента
        action_chains.drag_and_drop(element_to_drag, target_location).perform()

    @allure.step('Ожидаем исчезновения текста в элементе')
    def is_disappeared(self, locator, text_in_element):
        WebDriverWait(
            self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text_in_element))

    @allure.step("Найти все элементы с ожиданием")
    def find_elements(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time) \
            .until(EC.presence_of_all_elements_located(locator),
                   message=f"Не найдены элементы = {locator}")





    # @allure.step("Получение текста элемента")
    # def get_text(self, locator, wait_time=10):
    #     element = self.wait_for_visibility(locator, wait_time)
    #     return element.text

    # @allure.step("Переключаемся на новую вкладку")
    # def switch_to_new_tab(self):
    #     main_window_handle = self.driver.current_window_handle
    #     new_tab_handle = None
    #     # Переключаемся на новую вкладку
    #     for window_handle in self.driver.window_handles:
    #         if window_handle != main_window_handle:
    #             new_tab_handle = window_handle
    #             break
    #     if new_tab_handle:
    #         self.driver.switch_to.window(new_tab_handle)

