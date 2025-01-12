from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def test_multiple_matches_fails(page: Page):
    page.goto(BASE_URL)

    page.get_by_role('link').click()


def test_multiple_matches_first_last_nth(page: Page):
    page.goto(BASE_URL)

    buttons = page.get_by_role('link').click()

    print(buttons.first.text_content())
    print(buttons.last.text_content())
    print(buttons.nth(1).text_content())

def test_multiple_matches_count_or_iterate(page):
    page.goto(BASE_URL)
    page.get_by_role('button', name='Register').click()

    feedback = page.locator('.invalid-feedback')

    for message in feedback.all():
        expect(message).to_be_visible()