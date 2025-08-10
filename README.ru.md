# Playwright Automation Testing for Demoblaze

[![EN](https://img.shields.io/badge/EN-english-CC0000?logo=unitedkingdom&logoColor=white)](https://github.com/Ewerall/PlaywrightDemoblaze/blob/main/Readme.md)

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-FF4882?logo=allure&logoColor=white)](https://qameta.io/allure-report/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/Ewerall/PlaywrightDemoblaze/actions/workflows/ci.yml)

Автоматизация тестирования для веб-приложения [Demoblaze](https://demoblaze.com):
- **26+ параметризованных тестов** с полным покрытием функционала
- **End-to-End сценарии** реального пользовательского взаимодействия
- **Продвинутую работу с ожиданиями** для "сложных" веб-приложений
- Интеграцию с **Allure Report** и **GitHub Actions CI/CD**

## Особенности реализации

- **Устойчивый Page Object Model**  
  Адаптированный под сайты с плохой версткой и динамической загрузкой
- **Комбинированные стратегии ожиданий**  
  Сочетание сетевых ожиданий, кастомных JS-проверок и обработки диалогов
- **Параметризация тестовых данных**  
  Генерация реалистичных профилей с помощью Faker
- **Профессиональная Allure-интеграция**  
  Детализированные отчеты с эпиками, фичами и историями
- **Управление состоянием**  
  Фикстуры для очистки корзины и изоляции тестов

```bash
PlaywrightDemoblaze
├── .github/              # CI/CD конфигурация
├── data/                 # Генераторы тестовых данных
├── pages/                # Реализация Page Object Model
├── tests/                # 26+ параметризованных тестов
├── conftest.py           # Фикстуры и конфигурация
├── pytest.ini            # Настройки Pytest
└── requirements.txt      # Зависимости
```

## Технический стек

| Категория  | Технологии |
|--|--|
| Core | Python 3.10+, Playwright, Pytest |]
| Patterns | Page Object Model (POM)|
| Reporting| Allure Framework, Allure-pytest|
| CI/CD | GitHub Actions, Allure Report CI |
| Utilities | Faker (генерация данных) |

## Запуск тестов
```
# Установка зависимостей
pip install -r requirements.txt
playwright install

# Запуск всех тестов
pytest --alluredir=allure-results

# Запуск конкретной группы тестов
pytest tests/test_e2e.py -v

# Генерация Allure отчета
allure serve allure-results
```
## Allure-отчеты
[Последний Allure-отчет](https://ewerall.github.io/PlaywrightDemoblaze/#suites/ac0d5a5ca3595f3896d8c76597ca74f3/3c820b7c61d675ab/ "Allure") из Github actions

##  Ключевые тест-кейсы
Тип тестирования |	Примеры сценариев |	Кол-во
|--|--|--|
End2End | Регистрация → Выбор товаров → Оплата | 1+
Главная страница |Категории, карусель, пагинация | 3+ 	
Страница товара | Проверка данных, добавление в корзину | 2+
Корзина	| Расчет сумм, удаление, оформление | 1+
Пользователи |Регистрация, вход, фидбэк | 2+
Невалидные значения | Регистрация, вход, фидбэк, заказ | 4+

## Решенные технические вызовы

1. Работа с "хрупкими" элементами <br>
Кастомные ожидания для динамически загружаемого контента:
```python
with  self.page.expect_response(lambda  response: '/pagination'  in  response.url  and  response.status  ==  200):
        self.page.locator(direction).click()
self.page.wait_for_function("""
	() => {
            const container = document.querySelector('#tbodyid');
            return container && container.children.length > 0;
        }
""", timeout=10000)
expect(self.page.locator("#tbodyid .col-lg-4").first).to_be_visible(timeout=10000)
```
2. Обработка диалогов и алертов <br>
Специализированные обработчики для модальных окон:

```python
with page.expect_event("dialog") as dialog_info:
    page.locator(ADD_BUTTON).click()
dialog = dialog_info.value
dialog.accept()
```

3. Сетевые ожидания <br>
Контроль API-запросов во время действий:

```python
with  self.page.expect_response("**/bycat") as  response_info:
	self.page.click(f'a:has-text("{category}")')
response  =  response_info.value
assert  response.status  ==  200
```

## Пример запуска в headed режиме

<video src='https://github.com/user-attachments/assets/1c503fa2-f8ec-4cfc-a1f5-7eefd5123ff6' width=180/>
