from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def check_console_event(event):
    if event.type == 'error':
        raise AssertionError(f'Console error found: {event.text}')

def test_check_console(page: Page):

    print('')
    page.on('console', lambda msg: print(msg.text))
    page.on('pageerror', lambda msg: print(msg))

    # Failowanie testu jeśli złapie błąd w konsoli
    # Rozwiązanie które zwraca cały długi stack po teście
    # page.on('console', check_console_event)

    # Prostrze rozwiązanie
    console_errors = []
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)


    page.goto(BASE_URL)

    page.get_by_role('button', name='Register').click()

    assert len(console_errors) == 0, 'Expected 0 console errors'


def test_check_console_error(page: Page):

    page.goto(BASE_URL)
    page.get_by_role('button', name='Register').click()
