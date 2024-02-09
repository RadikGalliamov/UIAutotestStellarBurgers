import allure
import pytest

from data import TestDataUrl
from pages.main_page import MainPageHelper
from locators.main_page_locators import MainPageLocators

"""
Проверка основного функционала
Проверь:
переход по клику на «Конструктор»,
переход по клику на «Лента заказов»,
если кликнуть на ингредиент, появится всплывающее окно с деталями,
всплывающее окно закрывается кликом по крестику,
при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
залогиненный пользователь может оформить заказ.
"""


class TestMainPage:
    @allure.title('переход по клику на «Конструктор»')
    @allure.description("")
    def test_click_on_constructor(self, driver):
        page = MainPageHelper(driver)
        page.open_url(TestDataUrl.LOGIN_PAGE_URL)
        page.click_on_the_constructor_button()
        assert page.find_text_assemble_the_burger(), "Не найден элемент текст 'Собери бургер'"
