import pytest
from playwright.sync_api import Page, Browser, Playwright
from time import sleep


def test_page_fixture(page: Page):
    name_input = page.get_by_label('First name')

# Playwright > BrowserType > Browser > Context (v container) > Page (tab)
def test_different_browsers(playwright: Playwright):
    chromium_page = playwright.chromium.launch().new_context().new_page()
    firefox_page = playwright.firefox.launch(slow_mo=2000, headless=False).new_context().new_page()


def test_browser(browser: Browser):
    ctx = browser.new_context(
        viewport={'width': 400, 'height': 200},
        locale='es_ES',
        base_url='https://google.com'
    )
    page = ctx.new_page()
    page.goto('')
    sleep(2)
    page.screenshot(path='result.png')


def test_browser_type(page: Page):
    pass


def test_incomplete_fixture_name(playwright: Playwright, page: Page):
    pass



