from .basepage import Basepage
from playwright.sync_api import expect
import allure

class Cartpage(Basepage):
    PRICES = "#tbodyid tr td:nth-child(3)"
    DELETE = "#tbodyid tr:first-child td:nth-child(4) a"
    PLACE_ORDER = 'Place Order'
    MODAL_DIALOG = '.modal-content'
    NAME = '#name'
    COUNTRY = '#country'
    CITY = '#city'
    CARD = '#card'
    MONTH = '#month'
    YEAR = '#year'
    PURCHASE = '.modal-footer >> button:has-text("Purchase")'
    CANCEL = '.modal-footer >> button:has-text("Close")'
    CONFIRM_BUTTON = '.sa-confirm-button-container >> button:has-text("OK")'

    @allure.step("Получаем стоимость всех товаров в корзине")
    def get_total_price(self):
        prices = []
        price_elements = self.page.locator(self.PRICES).all()

        for element in price_elements:
            text = element.text_content().strip()
            prices.append(float(text))
        
        return sum(prices) 
    
    @allure.step("Удаляем первый товар в корзине")
    def delete_first_product(self):
        self.page.locator(self.DELETE).first.wait_for()
        
        with self.page.expect_response(lambda response: '/deleteitem' in response.url and response.status == 200):
            with self.page.expect_navigation():
                self.page.locator(self.DELETE).first.click()
        
        self.page.wait_for_load_state("load")
    
        expect(self.page.locator("body")).to_be_visible()

    @allure.step("Заполняем форму оформления заказа")
    def send_order(self, data: dict):
        try:
            self.page.get_by_role('button', name=self.PLACE_ORDER).click()
            self.page.locator(self.MODAL_DIALOG, has_text="Place order").wait_for(state="visible", timeout=2000)

            self.page.locator(self.NAME).fill(data['name'])
            self.page.locator(self.COUNTRY).fill(data['country'])
            self.page.locator(self.CITY).fill(data['city'])
            self.page.locator(self.CARD).fill(data['card'])
            self.page.locator(self.MONTH).fill(data['month'])
            self.page.locator(self.YEAR).fill(data['year'])
            
            self.page.locator(self.PURCHASE).click()

            self.page.wait_for_selector(self.CONFIRM_BUTTON, state = 'visible')
            self.page.wait_for_timeout(500) #without this -> no redirect to homepage, idk why
            self.page.locator(self.CONFIRM_BUTTON).click()
            
            self.page.wait_for_url("**/index.html", timeout=10000)
    
            return True
            
        except Exception as e:
            print(f"Error during send_order: {e}")
            return False


