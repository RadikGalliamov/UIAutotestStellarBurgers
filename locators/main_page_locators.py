from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    - HEADER
    """
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка Конструктор
    PERSONAL_CABINET_TEXT = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")  # Кнопка Лента заказов

    """
    - MAIN AREA
    """
    ASSEMBLE_THE_BURGER_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Текст 'Соберите бургер'

    ORDER_FEED_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")  # Текст 'Лента заказов'

    INGREDIENT_BUN = (
        By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # Ингредиент Флюоресцентная булка R2-D3

    INGREDIENT_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")  # Текст 'Детали ингредиента'

    INGREDIENT_DETAILS_CLOSE = (
        By.XPATH, "(.//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    # Закрыть всплывающее окно 'Детали ингредиента'

    ORDER_AREA = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # Область заказа

    BUN_INGREDIENT_COUNTER = (
        By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[starts-with(@class,'counter')]")
    # Счетчик ингредиента булка

    MAKE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка 'Оформить заказ'

    MODAL_WINDOW_ID_ORDER = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")
    # модальное окно 'Идентификатор заказа'

    ANY_ORDER_IN_ORDER_FEED = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    # один любой заказ из списка заказов в 'Ленте заказов'

    MODAL_WINDOW_ORDER_IN_ORDER_FEED = (By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    # Модальное окно заказа в 'Ленте заказов'

    ID_ORDER_IN_MODAL_WINDOW = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    # номер заказа в модальном окне 'Идентификатор заказа'

    CLOSE_ID_ORDER_MODAL_WINDOW = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # крестик для закрытия модального окна 'Идентификатор заказа'

    ALL_ORDERS_IN_HISTORY_ORDERS = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # все заказы пользователя в разделе 'История заказов'

    ALL_ORDERS_IN_ORDER_FEED = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # все заказы пользователя в разделе 'Лента заказов'

    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")
    # счетчик выполнено за все время заказов в 'Ленте Заказов'

    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")
    # счетчик 'Выполнено за сегодня' заказов в 'Ленте Заказов'

    IN_WORK_FEED_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
    # id заказа в статусе 'В работе' в разделе 'Ленте Заказов'

    """
    - FOOTER
    """
