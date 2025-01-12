from playwright.sync_api import expect, Page

from tests.utils.constants import BASE_URL


def test_check(page: Page):
    page.goto(BASE_URL)

    checkbox = page.get_by_role('checkbox')
    textarea = page.locator('#textarea')
    message = 'msg'

    checkbox.check()
    textarea.fill(message)

    expect(textarea).to_have_value(message)