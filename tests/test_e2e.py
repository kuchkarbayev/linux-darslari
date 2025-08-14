import pytest
import allure

from pages.homepage import Homepage
from pages.productpage import Productpage
from pages.cartpage import Cartpage
from data.data import generate_fake_data


@allure.epic("Demoblaze")
@allure.feature("E2E тестирование")
@allure.story("Тестирование по пользовательскому сценарию #1")
@pytest.mark.parametrize("product_name1, product_name2", [
    ('Apple monitor 24', 'Nokia lumia 1520'),
    ('MacBook air', 'Iphone 6 32gb'),
    ('Dell i7 8gb', 'Sony vaio i5'),
])
def test_e2e_one(page, product_name1, product_name2):
    home_page = Homepage(page)
    product_page = Productpage(page)
    cart_page = Cartpage(page)
    fake_data = generate_fake_data()

    with allure.step("Регистрируем аккаунт"):
        home_page.sign_up(fake_data)

    with allure.step("Вход в аккаунт"):
        home_page.log_in(fake_data)

    with allure.step("Переходим на следующую страницу товаров"):
        home_page.table_page('#next2')

    with allure.step("Переходим на карточку товара {product_name1}"):
        home_page.go_to_product(product_name1)

    with allure.step("Добавляем {product_name1} в корзину"):
        product_page.add_to_cart()

    with allure.step("Возращаемся на главную страницу"):
        product_page.back_home()

    with allure.step("Переходим на карточку товара {product_name2}"):
        home_page.go_to_product(product_name2)

    with allure.step("Добавляем {product_name2} в корзину"):
        product_page.add_to_cart()

    with allure.step("Переходим в корзину"):
        product_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page.send_order(fake_data)

    with allure.step("Заполняем форму и отправляем"):
        result = home_page.contact_window(fake_data)
        assert result is True
