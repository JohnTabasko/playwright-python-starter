import pprint
from time import sleep
from playwright.sync_api import Playwright
from pprint import pprint


def test_geolocation(playwright: Playwright):

    # Do emulacji urządzenia
    # ipad: dict = playwright.devices['iPad Pro 11']
    # pprint(playwright.devices)

    ctx = playwright.chromium.launch(headless=False, slow_mo=1000).new_context(
        # **ipad,
        # Zamiast emulacji urządzenia można utworzyć agenta, który zachowa
        # się tak jak emulator
        user_agent='Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X)'
                    'AppleWebKit/605.1.15 (KHTML, like Gecko)'
                    'Version/18.0 Mobile/15E148 Safari/604.1',
        locale='en_GB',
        geolocation={"longitude": -0.118092, "latitude": 51.509865},
        permissions=["geolocation"],
        base_url='https://maps.google.com'
    )

    page = ctx.new_page()
    page.goto('')
    page.get_by_role('button', name='Accept all').click()
    page.get_by_role('button', name='Stay on web').click()
    sleep(2)