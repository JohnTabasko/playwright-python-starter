from time import sleep

from playwright.sync_api import Page, BrowserType


# Code > CLI > config
def test_override_example(page: Page, browser_type: BrowserType):
    response = page.goto('')
    print(response.url)

    browser_type.launch(headless=False).new_context(
        base_url='https://playwright.dev/python/'
    ).new_page().goto('')
    sleep(2)