from faker import Faker
import pytest
import allure

from pages.homepage import Homepage
from pages.cartpage import Cartpage
from data.data import generate_fake_data

fake = Faker()


@allure.epic("Demoblaze")
@allure.feature("Тестирование невалидных значений")
@allure.story("Проверка обработки невалидных значений функции Sign Up")
@pytest.mark.parametrize("data, expect_result", [
    ({'username': 'admin'}, False),
    ({'username': ''}, False),
    ({'username': fake.password(length=100)}, False),
    ({'username': fake.password(length=10, special_chars=True, digits=False,
                                upper_case=True, lower_case=True)}, False),
])
def test_invalid_signup(page, data, expect_result):
    home_page = Homepage(page)

    with allure.step("Пытаемся регистрировать аккаунт"):
        assert home_page.sign_up(data) == expect_result


@allure.epic("Demoblaze")
@allure.feature("Тестирование невалидных значений")
@allure.story("Проверка обработки невалидных значений функции Log in")
@pytest.mark.parametrize("data, expect_result", [
    ({'username': ''}, False),  # Empty
    ({'username': fake.user_name() + 'QAtest'}, False),  # Random user doesnt exist
    ({'username': 'admins'}, False),  # Wrong password
])
def test_invalid_login(page, data, expect_result):
    home_page = Homepage(page)

    with allure.step("Пытаемся войти в аккаунт"):
        assert home_page.log_in(data) == expect_result


@allure.epic("Demoblaze")
@allure.feature("Тестирование невалидных значений")
@allure.story("Проверка обработки невалидных значений функции Cart")
def test_cart_invalid(page):
    home_page = Homepage(page)
    cart_page = Cartpage(page)
    fake_data = generate_fake_data()

    with allure.step("Перейти в пустую корзину"):
        home_page.go_to_cart()

    with allure.step("Пробуем оформить пустой заказ"):
        result = cart_page.send_order(fake_data)
        assert result is False


@allure.epic("Demoblaze")
@allure.feature("Тестирование невалидных значений")
@allure.story("Проверка обработки невалидных значений функции Feedback")
def test_feedback_invalid(page, data={'email': '', 'name': '', 'message': ''}):
    home_page = Homepage(page)

    with allure.step("Отправить пустой feedback"):
        result = home_page.contact_window(data)
        assert result is False
