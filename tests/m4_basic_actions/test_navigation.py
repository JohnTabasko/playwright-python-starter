from playwright.sync_api import expect, Page

from tests.utils.constants import BASE_URL

home_title = 'Credit Association'
savings_title = 'Save with us'


def test_back_forward_reload(page: Page):
    page.goto(BASE_URL)
    page.goto(f'{BASE_URL}savings.html')
    expect(page).to_have_title(savings_title)

    page.go_back()
    expect(page).to_have_title(home_title)

    page.go_forward()
    expect(page).to_have_title(savings_title)

    page.reload()
    expect(page).to_have_title(savings_title)


def test_navigation(page: Page):
    page.goto(BASE_URL, wait_until='load', timeout=1000)
    expect(page).to_have_title(home_title)


def test_load_speed_while_navigating(page: Page):
    page.goto('')
    page.goto(f'savings.html', timeout=5000)
    expect(page).to_have_title(savings_title)

def test_challenge_32(page: Page):
    page.goto("http://localhost:8000/web/")
    page.get_by_role("button", name="Register").click()
    warning_messages = page.locator('.invalid-feedback')
    for message in warning_messages.all():
        expect(message).to_be_visible()
    page.reload()
    for message in warning_messages.all():
        expect(message).to_be_hidden()
