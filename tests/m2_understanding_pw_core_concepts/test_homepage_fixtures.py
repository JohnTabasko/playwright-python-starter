from playwright.sync_api import Page, expect

from tests.m1_introducing_playwright.browser_support import browser


def test_homepage_title(page: Page):
    page.goto('http://localhost:8000/')


def test_homepage_header(page: Page):
    page.goto('http://localhost:8000/')
    header = page.locator('h4')
    assert header.text_content() == 'Register to become a member'


def test_damian(page: Page):
    page.goto('http://localhost:8000')
    expected_message = '© 2025'
    copyright_locator = page.locator('copyright')
    page.wait_for_selector(copyright_locator, timeout=5000)
    actual_text = page.inner_text(copyright_locator)
    assert expected_message in actual_text

# def test_homepage_copyright(page: Page):
#     page.goto('http://localhost:8000/web')
#     copyright = page.locator('div[class="container"] span[id="copyright"]').inner_text()
#     print(f'Damian lubi w dupę {copyright}')
#     await expect(copyright).to_contain_text("© 2025")