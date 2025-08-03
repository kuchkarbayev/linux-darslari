from .basepage import Basepage
from playwright.sync_api import Dialog

class Productpage(Basepage):
    PRODUCT_NAME = 'name'
    ADD_BUTTON = '.btn btn-success btn-lg'

    def add_to_cart(self):

        def accept_alert(alert: Dialog):
            alert.accept()

        self.page.on('dialog', accept_alert)
        self.page.locator(self.ADD_BUTTON).click()
        self.page.wait_for_event('dialog')

    def get_product_name(self):
        return self.page.locator(self.PRODUCT_NAME).text_content() 