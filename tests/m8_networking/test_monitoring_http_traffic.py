from playwright.sync_api import expect, Page

from tests.utils.constants import BASE_URL


def test_monitoring_http_traffic(page: Page):
    page.on('request', lambda request: print(f'>> {request.method} {request.url}'))
    page.on('response', lambda response: print(f'>> {response.status} {response.url}'))

    page.goto(BASE_URL)

# challange - fail if response status code is >= 400
def test_http_traffic(page: Page):

    traffic_errors = []
    page.on('response',
            lambda response: traffic_errors.append(response) if response.status >= 400 else None)

    page.goto(BASE_URL)

    assert len(traffic_errors) == 0, 'Expected 0 traffic errors'

