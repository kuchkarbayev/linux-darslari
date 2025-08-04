from playwright.sync_api import Page, Dialog
from typing import TYPE_CHECKING
import allure

if TYPE_CHECKING:
    from pages.cartpage import Cartpage
    from pages.homepage import Homepage

class Basepage:
    CART_LINK = '#cartur'
    CART_ID = '#page-wrapper'
    CONTACT_LINK = 'a.nav-link[data-toggle="modal"][data-target="#exampleModal"]'
    CONTACT_EMAIL = '#recipient-email'
    CONTACT_NAME = '#recipient-name'
    CONTACT_MESSAGE = '#message-text'
    WINDOW = '.modal-dialog'
    CONTACT_SEND = '.modal-footer >> button:has-text("Send message")'
    LOG_LINK = '#login2'
    LOG_USER = '#loginusername'
    LOG_PASS = '#loginpassword'
    LOG_SEND = '.modal-footer >> button:has-text("Log in")'
    SIGN_LINK = '#signin2'
    SIGN_USER = '#sign-username'
    SIGN_PASS = '#sign-password'
    SIGN_SEND = '.modal-footer >> button:has-text("Sign up")'

    def __init__(self, page: Page):  
        self.page = page

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.page.locator(self.CART_LINK).click()
        self.page.locator(self.CART_ID).wait_for()
        
        from pages.cartpage import Cartpage
        return Cartpage(self.page)
    
    def contact_window(self, data: dict):
        alert_received = [False] 
        
        def alert_accept(alert: Dialog):
            alert_received[0] = True
            alert.accept()

        self.page.on('dialog', alert_accept)
        self.page.locator(self.CONTACT_LINK).click()
        self.page.locator(self.WINDOW, has_text = "New message").wait_for(state="visible", timeout=2000)

        self.page.locator(self.CONTACT_EMAIL).fill(data['email'])
        self.page.locator(self.CONTACT_NAME).fill(data['name'])
        self.page.locator(self.CONTACT_MESSAGE).fill(data['message'])

        self.page.locator(self.CONTACT_SEND).click()
        self.page.wait_for_timeout(500)
        self.page.remove_listener('dialog', alert_accept)

        return alert_received[0]
    
    def _open_auth_modal(self, link_selector: str, modal_title: str):
        self.page.locator(link_selector).click()
        self.page.locator(self.WINDOW, has_text=modal_title).wait_for(state="visible", timeout=2000)

    def _fill_and_submit(self, username: str, password: str, user_field: str, pass_field: str, submit_button: str):
        self.page.locator(user_field).fill(username)
        self.page.locator(pass_field).fill(password)
        self.page.wait_for_timeout(1000)
        self.page.locator(submit_button).click()

    @allure.step("Авторизация пользователя")
    def log_in(self, data: dict):
        self._open_auth_modal(self.LOG_LINK, "Log in")
        self._fill_and_submit(
            username=data['username'],
            password=data['username'],
            user_field=self.LOG_USER,
            pass_field=self.LOG_PASS,
            submit_button=self.LOG_SEND)

    @allure.step("Регистрация пользователя")
    def sign_up(self, data: dict):
        self._open_auth_modal(self.SIGN_LINK, "Sign up")
        self._fill_and_submit(
            username=data['username'],
            password=data['username'],
            user_field=self.SIGN_USER,
            pass_field=self.SIGN_PASS,
            submit_button=self.SIGN_SEND)
        
    @allure.step("Возвращаемся на главную страницу")        
    def back_home(self):
        self.page.get_by_role('link', name = 'Home').click()
        self.page.wait_for_url("https://demoblaze.com/index.html", timeout=1000)
        from pages.homepage import Homepage
        return Homepage(self.page)
