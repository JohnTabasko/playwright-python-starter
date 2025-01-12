from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def test_screenshot_demo(page: Page):

    page.goto(BASE_URL)
    name_input = page.get_by_label('First name')
    name_input.fill('Andrejs')
    page.get_by_role('button', name='Register').click()

    page.screenshot(path='screenshots/screenshot.png')

    elements_to_mask = page.locator('.form-control').all()
    page.screenshot(
        path='screenshots/screenshot-advanced.jpeg',
        full_page=True,
        mask=elements_to_mask,
        mask_color='blue'
    )

    feedback = page.locator('.invalid-feedback')

    for message in feedback.all():
        expect(message).not_to_be_visible()
