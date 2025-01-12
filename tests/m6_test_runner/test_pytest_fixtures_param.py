import pytest
from playwright.sync_api import expect, Page

from tests.utils.constants import BASE_URL


# Before Parameterization
def test_single_param_with_bob(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill('Bob')
    expect(name_input).to_have_value('Bob')

    # ...


def test_single_param_with_alexandrina(page: Page):
    page.goto('')

    name_input = page.get_by_label('First name')
    name_input.fill('Alexandrina')
    expect(name_input).to_have_value('Alexandrina')

    # ...


# After: to parameterize
@pytest.mark.parametrize('name', ['Bob',
                                  'Alexandrina',
                                  'Even_longer_name'])
def test_single_param(page: Page, name: str):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)

    # ...


# After: to parameterize with tuples
# @pytest.mark.parametrize('name', 'last_name', [
#     ('Bob', 'Smith', False, 123),
#     ('Aleksa', 'Johnson', True, 456)
# ])
# def test_two_params(page: Page, name: str, last_name: str):
#     page.goto(BASE_URL)
#
#     first_name_input = page.get_by_label('First name')
#     first_name_input.fill(name)
#     expect(first_name_input).to_have_value(name)
#
#     last_name_input = page.get_by_label('Last name')
#     last_name_input.fill(last_name)
#     expect(last_name_input).to_have_value(last_name)
