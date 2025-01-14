import pytest
from playwright.sync_api import expect, Page, Browser

from tests.utils.constants import BASE_URL


@pytest.fixture
def page(browser: Browser): # session scope
    print("Set up once for all tests")
    print(f"Browser hash: {hash(browser)}")

    page: Page = browser.new_context(
        viewport={'width': 500, 'height': 400},
        user_agent='xyz',
        locale='es_ES'
        # ...
    ).new_page()

    page.goto(BASE_URL)
    yield page

class TestThings:

    def test_one(self, page: Page):
        print(f"Page hash: {hash(page)}")
        name_input = page.get_by_label('First name')
        name_input.fill('Sofia')
        expect(name_input).to_have_value('Sofia')

    def test_two(self, page: Page):
        print(f"Page hash: {hash(page)}")
        name_input = page.get_by_label('First name')
        name_input.fill('Andrejs')
        expect(name_input).to_have_value('Andrejs')
