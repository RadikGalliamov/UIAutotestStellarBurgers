## Авто-тесты для проверки веб-приложения Stellar Burgers.

## Реализованные сценарии

### Восстановление пароля:

- проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"
- проверка ввода почты и клика по кнопке "Восстановить"
- проверка активности поля пароля при нажатии на кнопку показать/скрыть пароль

### Личный кабинет:

- проверка перехода по клику на "Личный кабинет"
- проверка перехода в раздел "История заказов"
- выход из аккаунта

### Проверка основного функционала:

- проверка перехода по клику на "Конструктор"
- проверка перехода по клику на "Лента заказов"
- проверка отображения детальной информации при клике на ингредиент
- проверка закрытия окна детальной информации при клике на крестик
- проверка увеличения счетчика ингредиентов при добавлении их в бургер
- проверка создания заказа авторизованным пользователем

### Лента заказов:

- проверка открытия детальной информации о заказе
- проверка отображения заказов пользователя на странице "Лента заказов"
- проверка увеличения счетчика "Выполнено за все время" при создании нового заказа
- проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа
- проверка отображения созданного заказа в разделе "В работе"

## Структура проекта

- `test_main_page.py` - тесты на проверку основного функционала сервиса
- `test_order_feed.py` - тесты на проверку ленты заказов
- `test_password_recovery_page.py` - тесты на проверку восстановления пароля
- `test_personal_cabinet.py` - тесты на проверку личного кабинета

- `locators` - пакет, содержащий локаторы веб-элементов соответствующих тестов
- `pages` - пакет, содержащий базовые методы, и методы для каждой веб-страницы
- `tests` - пакет, содержащий тесты, разделенные по классам
- `conftest.py` - файл, содержащий фикстуры для проекта
- `data.py` - файл, содержащий тестовые данные для проекта

### Запуск автотестов

> `pytest` - Запуск всех тестов 
> `pytest -v tests/test_order_feed.py` - Запуск тестов страницы 'Ленты заказов'

**Установка зависимостей**

> `pip install -r requirements.txt`

**Запуск авто-тестов и создание HTML-отчета о покрытии**

> `pytest tests --alluredir=allure_results` - генерировать Allure-отчёт
> `allure serve allure_results` - сформировать отчёт в формате веб-страницы

**Описание тестов **

@pytest.mark.ui 

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL) - BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

@allure.dynamic.title("Test Authentication")
@allure.dynamic.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.dynamic.tag("NewUI", "Essentials", "Authentication")
@allure.dynamic.severity(allure.severity_level.CRITICAL) - BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL
@allure.dynamic.label("owner", "John Doe")
@allure.dynamic.link("https://dev.example.com/", name="Website")
@allure.dynamic.issue("AUTH-123")
@allure.dynamic.testcase("TMS-456")