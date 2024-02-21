from selenium.webdriver.common.by import By


class PersonalCabinetPageLocators:
    """
    - HEADER
    """
    BUTTON_ORDER_HEADER = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")

    """
    - MAIN AREA
    """
    BUTTON_ORDER_MAIN_AREA = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    PROFILE_TEXT = (By.XPATH, "//a[text()='Профиль']")
    HISTORY_OF_ORDERS_TEXT = (By.XPATH, "//a[text()='История заказов']")
    HISTORY_OF_ORDERS_TEXT_ACTIVE = (
        By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='История заказов']")
    EXIT_TEXT = (By.XPATH, ".//button[@type='button' and text()='Выход']")