from .basepage import Basepage
from pages.productpage import Productpage

class Homepage(Basepage):
    SORT_CATEGORY = '.list-group-item'
    CAROUSEL_NEXT = '.carousel-control-next'
    CAROUSEL_PREV = '.carousel-control-prev'
    PREV_PAGE = "#prev2"
    NEXT_PAGE = "#next2"

    def __init__(self, page):
        super().__init__(page)
        self.link = "https://demoblaze.com/"

    def navigate(self):
        self.page.goto(self.link)
        self.page.wait_for_url(self.link)

    def sort_by_category(self, category: str):
        self.page.locator(self.SORT_CATEGORY, has_text = category).click()
        self.page.wait_for_load_state("domcontentloaded")
    
    def go_to_product(self, product: str): 
        original_url = self.page.url           
        self.page.get_by_role('link', name=product).click()
        self.page.wait_for_url(
            lambda url: url != original_url,  
            timeout=15000  
        )
        return Productpage(self.page)
    
    def verify_product(self, product_name: str):
        product_locator = self.page.get_by_role('link', name = product_name).count()
        if (product_locator > 0): return True
        else: return False

    def carousel_next(self):
        self.page.locator(self.CAROUSEL_NEXT).click()
        self.page.wait_for_timeout(1000)

    def carousel_prev(self):
        self.page.locator(self.CAROUSEL_PREV).click()
        self.page.wait_for_timeout(1000)   

    def previous_page(self):
        self.page.locator(self.PREV_PAGE).click()
        self.page.wait_for_timeout(1000)
    
    def next_page(self):
        self.page.locator(self.NEXT_PAGE).click()
        self.page.wait_for_timeout(1000)