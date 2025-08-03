from .basepage import Basepage
from playwright.sync_api import Dialog

class Cartpage(Basepage):
    PRICES = "#tbodyid tr td:nth-child(3)"
    DELETE = "#tbodyid tr:first-child td:nth-child(4)"
    PLACE_ORDER = 'Place Order'
    MODAL_DIALOG = '.modal-dialog'
    NAME = '#name'
    COUNTRY = '#country'
    CITY = '#city'
    CARD = '#card'
    MONTH = '#month'
    YEAR = '#year'
    PURCHASE = '.modal-footer >> button:has-text("Purchase")'
    CONFIRM_BUTTON = 'confirm btn btn-lg btn-primary'

    def get_total_price(self):
        self.page.locator(self.PRICES).first.wait_for()
        prices = []
        price_elements = self.page.locator(self.PRICES).all()

        for element in price_elements:
            text = element.text_content().strip()
            prices.append(float(text))
        
        return prices 
    
    def delete_first_product(self):
        self.page.locator(self.DELETE).first.wait_for()
        self.page.locator(self.DELETE).click()

    def send_order(self, data: dict):
        self.page.get_by_role('button', name = self.PLACE_ORDER).click()
        self.page.locator(self.MODAL_DIALOG).wait_for()

        self.page.locator(self.NAME).fill(data['name'])
        self.page.locator(self.COUNTRY).fill(data['country'])
        self.page.locator(self.CITY).fill(data['city'])
        self.page.locator(self.CARD).fill(data['card'])
        self.page.locator(self.MONTH).fill(data['month'])
        self.page.locator(self.YEAR).fill(data['year'])
        
        self.page.locator(self.PURCHASE).click
        self.page.locator(self.CONFIRM_BUTTON).first.wait_for()
        self.page.locator(self.CONFIRM_BUTTON).click()



