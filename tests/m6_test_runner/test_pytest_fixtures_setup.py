import pytest
import requests
from playwright.sync_api import expect, Page

from tests.utils.constants import BASE_URL


# @pytest.fixture
# def page(page: Page):
#
#     page.goto(BASE_URL)
#     return page



@pytest.fixture
def page(page: Page, once_per_module):

    page.goto(BASE_URL)
    yield page

    # do cleanup
    print('\ncleanup')

def test_single_param(page: Page):
    name_input = page.get_by_label('First name')
    name_input.fill('Sofia')
    expect(name_input).to_have_value('Sofia')


@pytest.mark.parametrize('name', ['Alice', 'Bob'])
def test_two_params(page: Page, name: str):
    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)
