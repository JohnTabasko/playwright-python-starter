import pytest
from playwright.sync_api import Page, Response, APIRequestContext, APIResponse, expect, Browser, Playwright

from tests.utils.constants import BASE_URL

@pytest.fixture(scope='module')
def once_per_module(playwright: Playwright):
    print('Run once for all tests')
    # challenge - replace with playwright
    ctx = playwright.request.new_context(base_url='https://api.github.com/users/adrejs-ps')
    yield ctx.get('name')

@pytest.fixture
def page(page: Page):
    page.goto(BASE_URL)
    yield page
    # do cleanup

def test_one(page: Page, once_per_module):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    print(f'Test 1: {once_per_module}')

def test_two(page: Page, once_per_module):
    name_input = page.get_by_label('First name')
    name_input.fill('name')
    expect(name_input).to_have_value('name')

    print(f'Test 2: {once_per_module}')
# def test_api_request_context(playwright: Playwright):
#
#     independent_api_ctx = playwright.request.new_context(base_url='...')
#
#     independent_api_ctx.get('your/api/url')