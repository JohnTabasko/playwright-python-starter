from pprint import pprint

from playwright.sync_api import expect, Page, APIResponse, Playwright, APIRequestContext, Response

from tests.utils.constants import BASE_URL


def test_api_request_response(page: Page):
    response: Response = page.goto(BASE_URL)
    print(response.url)
    print(response.status)
    print(response.ok) # 200-299

    pprint(response.all_headers()) # Dict[str, str]
    pprint(response.headers_array()) # List[NameValue]

    print(response.body()) # bytes
    print(response.text()) # string obj

    # print(response.json()) # throw error if not parseable json

    # request: Request = response.request
    # print(request.all_headers())
    # print(request.method)

def test_api_request_context(playwright: Playwright):
    pass
