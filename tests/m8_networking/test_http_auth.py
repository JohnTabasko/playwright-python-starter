import pytest
from playwright.sync_api import expect, APIRequestContext, Playwright, Page, APIResponse

# Constants
REPO = 'Playwright-Test-Repo'
USERNAME = 'JohnTabasko'  # Replace with your GitHub username
TOKEN = ''

@pytest.fixture(autouse=True)
def setup_and_teardown(playwright: Playwright):

    # create repo
    api_context: APIRequestContext = playwright.request.new_context(
        base_url='https://api.github.com/',
        extra_http_headers={
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {TOKEN}'
        }
    )

    response: APIResponse = api_context.post('user/repos', data={'name': REPO})
    expect(response).to_be_ok()

    yield

    # clean-up - zawsze po yield - nawet jeśli nie chcę nic zwracać,
    # yield jest separatorem między ustawieniem a czyszczeniem

    deletion_response = api_context.delete(f'repos/{USERNAME}/{REPO}')
    expect(deletion_response).to_be_ok()
    assert  deletion_response.status == 204, 'Failed to delete repo'


def test_work_with_newly_created_repo(page: Page):
    page.goto(f'https://github.com/{USERNAME}?tab=repositories')

    repo = page.get_by_role('link', name=REPO)
    expect(repo).to_have_count(1)

    # ...