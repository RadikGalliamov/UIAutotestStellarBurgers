import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPageHelper


@pytest.fixture(scope="function", params=["chrome"])  # params=["firefox", "chrome"]
def driver(request):
    if request.param == "firefox":
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
    if request.param == "chrome":
        chrome_driver = ChromeDriverManager().install()
        service = CS(chrome_driver)
        options = CO()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture()
def log_in(driver):
    LoginPageHelper(driver).login()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            # Сделать скриншот и добавить его в отчет
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
