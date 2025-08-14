import pytest
import allure

from pages.homepage import Homepage
from pages.productpage import Productpage


@allure.epic("Demoblaze")
@allure.feature("Тестирование страницы продукта")
@allure.story("Проверка соответствия названия товара с указаным на странице")
@pytest.mark.parametrize("product_name", [
    ('Samsung galaxy s6'),
    ('Sony vaio i7'),
    ('Iphone 6 32gb'),
    ('HTC One M9')
])
def test_product_name(page, product_name):
    home_page = Homepage(page)
    product_page = Productpage(page)

    with allure.step("Переходим на страницу {product_name}"):
        home_page.go_to_product(product_name)

    with allure.step("Сохраняем название товара со страницы"):
        name = product_page.get_product_name()

    with allure.step("Сравниваем заданное и указанное название"):
        assert name == product_name


@allure.epic("Demoblaze")
@allure.feature("Тестирование страницы продукта")
@allure.story("Добавление товара в корзину")
@pytest.mark.parametrize("product_name", [
    ('Nokia lumia 1520'),
    ('Sony xperia z5'),
    ('Samsung galaxy s7'),
    ('Nexus 6')
])
def test_add_cart(page, product_name):
    home_page = Homepage(page)
    product_page = Productpage(page)

    with allure.step("Переходим на страницу {product_name}"):
        home_page.go_to_product(product_name)

    with allure.step("Нажимаем кнопку Add to cart"):
        result = product_page.add_to_cart()

    with allure.step("Получаем ответ"):
        assert result is True
