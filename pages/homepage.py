from .basepage import Basepage
from pages.productpage import Productpage
from playwright.sync_api import expect
import allure

class Homepage(Basepage):
    SORT_CATEGORY = '.list-group-item'
    PRODUCT_GRID = '#tbodyid'
    NAME_CARD = '#tbodyid > div:first-child .card-title .hrefch'
    CAROUSEL_NEXT = '.carousel-control-next'
    CAROUSEL_PREV = '.carousel-control-prev'
    PREV_PAGE = "#prev2"
    NEXT_PAGE = "#next2"
    
    @allure.step("Сортируем по категории {category}")
    def sort_by_category(self, category: str):
        self.page.locator(self.SORT_CATEGORY, has_text = category).click()
        with self.page.expect_response("**/bycat") as response_info:
            self.page.click(f'a:has-text("{category}")')

        response = response_info.value
        assert response.status == 200
        
        expect(self.page.locator("#tbodyid .card").first).to_be_visible(timeout=10000)
        
        self.page.wait_for_function("""
            () => {
                const container = document.querySelector('#tbodyid');
                return container && container.children.length > 0;
            }
        """, timeout=10000)

    @allure.step("Переходим в карточку товара {product}")
    def go_to_product(self, product: str):         
        self.page.get_by_role('link', name = product).click()
        self.page.wait_for_url("**/prod.html**", timeout=1000)
        return Productpage(self.page)
    
    def verify_product(self, product_name: str):
        return self.page.get_by_role('link', name = product_name).is_visible()

    @allure.step("Крутим карусель вперед")
    def carousel(self, direction):
        self.page.locator(direction).click()
        self.page.wait_for_timeout(1000) #need for animation
        
    @allure.step("Переходим на другую страницу товара")
    def table_page(self, direction):
        with self.page.expect_response(lambda response: '/pagination' in response.url and response.status == 200):
            self.page.locator(direction).click()
        
        self.page.wait_for_function("""
            () => {
                const container = document.querySelector('#tbodyid');
                return container && container.children.length > 0;
            }
        """, timeout=10000)
        
        expect(self.page.locator("#tbodyid .col-lg-4").first).to_be_visible(timeout=10000)