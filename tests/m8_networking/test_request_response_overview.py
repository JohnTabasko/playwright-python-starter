from pprint import pprint

from playwright.sync_api import Page, Response, APIRequestContext, APIResponse, expect, Browser, Playwright

from tests.utils.constants import BASE_URL


def test_request_response_overview(page: Page, browser: Browser):

    # browser.new_context().request
    response: Response = page.goto(BASE_URL)

    api_ctx: APIRequestContext = page.request

    api_response: APIResponse = api_ctx.get('https://api.github.com/')

    print(api_response.ok)
    print(api_response.status)
    pprint(api_response.headers_array)
    pprint(api_response.json())

    expect(api_response).to_be_ok() # works
    # expect(response).to_be_ok() # not works

def test_api_request_context(playwright: Playwright):

    independent_api_ctx = playwright.request.new_context(base_url='...')

    independent_api_ctx.get('your/api/url')