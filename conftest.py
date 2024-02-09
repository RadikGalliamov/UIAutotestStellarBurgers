import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import TestLoginPageData, TestDataUrl
from locators.login_page_locators import LoginPageLocators


# Запуск браузера
@pytest.fixture(params=["firefox", "chrome"])  # params=["firefox", "chrome"]
def driver(request):
    if request.param == "firefox":
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
    if request.param == "chrome":
        chrome_driver = ChromeDriverManager().install()
        service = CS(chrome_driver)
        options = CO()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


# @pytest.fixture()
# def log_in(driver):
#     driver.get(TestDataUrl.LOGIN_PAGE_URL)
#     driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(TestLoginPageData.email)
#     driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(TestLoginPageData.password)
#     driver.find_element(*LoginPageLocators.ENTER).click()
#     return driver
