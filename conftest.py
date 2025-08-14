import pytest
import allure
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://demoblaze.com/", wait_until='load')
        expect(page.locator("body")).to_be_visible()
        yield page
        if hasattr(pytest, "test_failed") and pytest.test_failed:
            allure.attach(
                page.screenshot(full_page=True),
                name=f"screenshot_{pytest.current_test_name}",
                attachment_type=allure.attachment_type.PNG
            )
        browser.close()
