from playwright.sync_api import Page

from tests.utils.constants import BASE_URL


def test_cookies(page: Page):
    page.goto(BASE_URL)

    print(page.context.cookies())

    page.context.add_cookies([{
        'name': 'cookie1',
        'value': 'abc',
        'url': 'https://playwright/dev/python/'
    }])

    print(page.context.cookies())

    page.context.clear_cookies()

    print(page.context.cookies())