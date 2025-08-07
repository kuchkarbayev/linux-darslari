from pages.homepage import Homepage
from pages.productpage import Productpage
from pages.cartpage import Cartpage
from data.data import generate_fake_data
import pytest 
import allure 

@allure.epic("Demoblaze")
@allure.feature("Тестирование корзины")
@allure.story("Сравнение цены товаров с заявленной в заказе и оформление заказа")
def test_check_price_cart(page):
    fake_data = generate_fake_data()

    home_page = Homepage(page)
    product_page = Productpage(page)
    cart_page = Cartpage(page)

    with allure.step("Переходим на карточку товара"):
        home_page.go_to_product("Samsung galaxy s6")
        
    with allure.step("Добавляем в корзину"):
        product_page.add_to_cart()

    with allure.step("Добавляем в корзину еще раз"):
        product_page.add_to_cart()

    with allure.step("Переходим в корзину"):
        product_page.go_to_cart()

    with allure.step("Проверяем цену с итоговой"):
        page.wait_for_function("document.querySelector('#totalp').textContent.trim() !== ''", timeout=10000)
        total = cart_page.get_total_price()
        assert total == float(page.locator("#totalp").inner_text())

    with allure.step("Удаление первого товара"):
        cart_page.delete_first_product()

    with allure.step("Оформление заказа"):
        result = cart_page.send_order(fake_data)
        assert result == True
        


