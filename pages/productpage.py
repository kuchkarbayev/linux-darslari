from .basepage import Basepage
from playwright.sync_api import Dialog
import allure

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages.homepage import Homepage

class Productpage(Basepage):
    PRODUCT_NAME = '.name'
    ADD_BUTTON = 'a.btn.btn-success.btn-lg'

    @allure.step("Добавляем товар в корзину")  
    def add_to_cart(self):
        alert_received = [False] 
        
        def accept_alert(alert: Dialog):
            alert_received[0] = True
            alert.accept()

        self.page.on('dialog', accept_alert)
        self.page.locator(self.ADD_BUTTON).click()
        self.page.wait_for_timeout(1000)
        
        self.page.remove_listener('dialog', accept_alert)
        
        return alert_received[0]
    
    @allure.step("Получаем имя товара в карточке")         
    def get_product_name(self):
        return self.page.locator(self.PRODUCT_NAME).text_content().strip()