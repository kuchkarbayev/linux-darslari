from pages.homepage import Homepage
import pytest 
import allure 

@pytest.mark.parametrize("category, product_name, expect_result", [
    ('Phones', 'Samsung galaxy s6', True),
    ('Phones', 'Sony vaio i7', False),
    ('Laptops', 'Sony vaio i5', True),
    ('Laptops', 'Nexus 6', False),
    ('Monitors', 'Apple monitor 24', True),
    ('Monitors', 'Dell i7 8gb', False)
])
def test_change_category(page, category, product_name, expect_result):
    home_page = Homepage(page)
    home_page.navigate()

    home_page.sort_by_category(category)

    page.wait_for_timeout(2000)

    assert home_page.verify_product(product_name) == expect_result

def test_next_carousel(page):
    home_page = Homepage(page)

    home_page.navigate()

    first_slide = page.locator(".carousel-item.active")
    first_slide_alt = first_slide.locator("img").get_attribute("alt")

    home_page.carousel_next()

    second_slide = page.locator(".carousel-item.active")
    second_slide_alt = second_slide.locator("img").get_attribute("alt")

    assert first_slide_alt != second_slide_alt

def test_prev_carousel(page):
    home_page = Homepage(page)

    home_page.navigate()

    first_slide = page.locator(".carousel-item.active")
    first_slide_alt = first_slide.locator("img").get_attribute("alt")

    home_page.carousel_prev()

    second_slide = page.locator(".carousel-item.active")
    second_slide_alt = second_slide.locator("img").get_attribute("alt")

    assert first_slide_alt != second_slide_alt

def test_next_table(page):
    home_page = Homepage(page)
    home_page.navigate()

    first_product_before = page.locator(".card-title a").first.inner_text()

    home_page.next_page()
    
    first_product_after = page.locator(".card-title a").first.inner_text()

    assert first_product_before != first_product_after
