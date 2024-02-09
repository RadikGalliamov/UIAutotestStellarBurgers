import allure
import pytest

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
    def test_questions_about_important(self, driver, question_locator, answer_locator, expected_text):
        page = MainPageHelper(driver)
        page.open()
        pass
