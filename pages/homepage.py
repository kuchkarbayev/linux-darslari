from .basepage import Basepage
from pages.productpage import Productpage
from playwright.sync_api import expect
import allure

class Homepage(Basepage):
    SORT_CATEGORY = '.list-group-item'
    PRODUCT_GRID = '#tbodyid'
    CAROUSEL_NEXT = '.carousel-control-next'
    CAROUSEL_PREV = '.carousel-control-prev'
    PREV_PAGE = "#prev2"
    NEXT_PAGE = "#next2"
    
    @allure.step("Сортируем по категории {category}")
    def sort_by_category(self, category: str):
        #initial_content = self.page.locator(self.PRODUCT_GRID).text_content()
        self.page.locator(self.SORT_CATEGORY, has_text = category).click()
        '''
        im tried everything, but this site absolutly bullshit, so idk, im just use implicit waits
        or it will be todo for better days
        try:
            self.page.wait_for_function(
                """(args) => {
                    const selector = args[0];
                    const initialText = args[1];
                    const currentElement = document.querySelector(selector);
                    const currentText = currentElement ? currentElement.textContent : '';
                    // console.log('Initial:', initialText, 'Current:', currentText); // Для отладки
                    return currentText !== initialText;
                }""",
                [self.PRODUCT_GRID, initial_content],
                timeout=10000)
        except Exception as e:
            print(f"Warning: wait_for_function failed or timed out: {e}")
        '''
        self.page.wait_for_timeout(2000) # spongebob crying

    @allure.step("Переходим в карточку товара {product}")
    def go_to_product(self, product: str):         
        self.page.get_by_role('link', name = product).click()
        self.page.wait_for_url("**/prod.html**", timeout=1000)
        return Productpage(self.page)
    
    def verify_product(self, product_name: str):
        product_locator = self.page.get_by_role('link', name = product_name).count()
        if (product_locator > 0): return True
        else: return False

    @allure.step("Крутим карусель вперед")
    def carousel(self, direction):
        '''
        initial_active_slide = self.page.locator(".carousel-item.active")
        initial_alt = initial_active_slide.locator("img").get_attribute("alt")
        self.page.locator(self.CAROUSEL_NEXT).click()
        try:
            expect(initial_active_slide).not_to_have_class("active", timeout=5000)
        except:
            expect(self.page.locator(".carousel-item.active img:not([alt='%s'])" % initial_alt)).to_be_visible(timeout=5000)
        '''
        self.page.locator(direction).click()
        self.page.wait_for_timeout(1000)

    @allure.step("Переходим на следующую страницу карточек товаров")
    def previous_page(self):
        self.page.locator(self.PREV_PAGE).click()
        self.page.wait_for_timeout(1000)

    @allure.step("Переходим на предыдущую страницу карточек товаров")    
    def next_page(self):
        self.page.locator(self.NEXT_PAGE).click()
        self.page.wait_for_timeout(1000)