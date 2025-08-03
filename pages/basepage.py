from playwright.sync_api import Page
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cartpage import CartPage

class Basepage:
    CART_LINK = '#cartur'
    CART_ID = '#page-wrapper'

    def __init__(self, page: Page):  
        self.page = page

    def go_to_cart(self):
        self.page.locator(self.CART_LINK).click()
        self.page.locator(self.CART_ID).wait_for()
        
        from cartpage import CartPage
        return CartPage(self.page)