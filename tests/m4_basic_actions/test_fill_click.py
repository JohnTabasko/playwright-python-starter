from playwright.sync_api import Page

from tests.utils.constants import BASE_URL


def test_fill(page: Page):
    page.goto(BASE_URL)

    page.get_by_label('First name').fill('Kamil')

    page.get_by_label('Date of birth').fill('1999-10-09')


def test_click_demo(page: Page):
    page.goto(BASE_URL)
    btn = page.get_by_role('button', name='Register')
