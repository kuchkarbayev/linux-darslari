from pages.homepage import Homepage
from data.data import generate_fake_data
import pytest 
import allure 

@allure.epic("Demoblaze")
@allure.feature("Тестирование регистрации и авторизации")
@allure.story("Создание аккаунта и вход")
def test_log_sign(page):
    home_page = Homepage(page)
    fake_data = generate_fake_data()

    with allure.step("Регистрируем аккаунт"):
        home_page.sign_up(fake_data)
    
    with allure.step("Вход в аккаунт"):
        home_page.log_in(fake_data)

    with allure.step("Проверяем вход в аккаунт"):
        result = page.get_by_role('link', name = 'Log out').count()
        assert result > 0

@allure.epic("Demoblaze")
@allure.feature("Тестирование feedback")
@allure.story("Отправка feedback с тестовыми данными")
def test_feedback(page):
    home_page = Homepage(page)
    fake_data = generate_fake_data()

    with allure.step("Заполняем форму и отправляем"):
        result = home_page.contact_window(fake_data)
        assert result == True
    