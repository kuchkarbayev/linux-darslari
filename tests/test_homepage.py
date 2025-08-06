from pages.homepage import Homepage
import pytest 
import allure 

@allure.epic("Demoblaze")
@allure.feature("Тестирование главной страницы")
@allure.story("Сортировка товаров по категориям")
@pytest.mark.parametrize("category, product_name, expect_result", [
    ('Phones', 'Samsung galaxy s6', True), #Valid data
    ('Phones', 'Sony vaio i7', False), #Invalid data
    ('Laptops', 'Sony vaio i5', True),
    ('Laptops', 'Nexus 6', False),
    ('Monitors', 'Apple monitor 24', True),
    ('Monitors', 'Dell i7 8gb', False)
])
def test_change_category(page, category, product_name, expect_result):
    home_page = Homepage(page)

    with allure.step("Нажимаем на категорию {category}"):    
        home_page.sort_by_category(category)

    with allure.step("Проверяем, что список товаров отсортировался"):    
        assert home_page.verify_product(product_name) == expect_result

@allure.epic("Demoblaze")
@allure.feature("Тестирование главной страницы")
@allure.story("Проверка кнопки карусели Вперед")
@pytest.mark.parametrize("direction", [
    ('.carousel-control-next'),
    ('.carousel-control-prev')
])
def test_carousel(page, direction):
    home_page = Homepage(page)

    with allure.step("Сохраняем alt изображения"):  
        first_slide = page.locator(".carousel-item.active")
        first_slide_alt = first_slide.locator("img").get_attribute("alt")

    with allure.step("Нажимаем кнопку карусели Вперед"):  
        home_page.carousel(direction)

    with allure.step("Сохраняем alt нового изображения"):  
        second_slide = page.locator(".carousel-item.active")
        second_slide_alt = second_slide.locator("img").get_attribute("alt")

    with allure.step("Сравниваем прошлое и настоящее изображение в каруселе"):  
        assert first_slide_alt != second_slide_alt

@allure.epic("Demoblaze")
@allure.feature("Тестирование главной страницы")
@allure.story("Проверка перехода на другую страницу карточек товаров")
def test_next_table(page):
    home_page = Homepage(page)

    with allure.step("Сохраняем текст первого товара"):  
        first_product_before = page.locator(".card-title a").first.inner_text()

    with allure.step("Переходим на следующую страницу"):  
        home_page.table_page('#next2')

    with allure.step("Сохраняем текст первого товара на новой странице"):  
        first_product_after = page.locator(".card-title a").first.inner_text()

    with allure.step("Сравниваем сохраненый текст"):  
     assert first_product_before != first_product_after
