import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    @allure.step('Создаем объекта класса BasePage')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)  # опрос страницы раз в секунду

    @allure.step("Открыть страницу по URL")
    def _open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент с ожиданием")
    def _find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time) \
            .until(EC.presence_of_element_located(locator),
                   message=f"Не найден элемент = {locator}")

    @allure.step("Ожидание и клик по элементу")
    def _wait_and_click(self, locator, wait_time=10):
        element = self._find_element(locator, wait_time)
        element.click()

    @allure.step("Ожидание видимости элемента")
    def _wait_for_visibility(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}")
        return element

    @allure.step("Ожидание кликабельного элемента")
    def _wait_for_clickable(self, locator, wait_time=10):
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
    def _not_find_element(self, locator, time=30):
        return WebDriverWait(
            self.driver, time
        ).until(
            EC.none_of(
                EC.visibility_of_element_located(locator)
            ),
            message=f'Элемент найден'
        )

    @allure.step("Переместить элемент на другое место на странице")
    def _drag_and_drop_element(self, element_to_drag, target_location):
        action_chains = ActionChains(self.driver)
        # Выполнение действия перетаскивания и бросания элемента
        action_chains.drag_and_drop(element_to_drag, target_location).perform()

    @allure.step('Ожидаем исчезновения текста в элементе')
    def _is_disappeared(self, locator, text):
        # Ожидаем, пока исчезнет исходный текст из элемента
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(locator, text)
        )
        # Ожидаем, пока текст элемента изменится
        WebDriverWait(self.driver, 10).until(
            lambda driver: self._find_element(locator).text.strip() != text
        )

    @allure.step("Найти все элементы с ожиданием")
    def _find_elements(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time) \
            .until(EC.presence_of_all_elements_located(locator),
                   message=f"Не найдены элементы = {locator}")





