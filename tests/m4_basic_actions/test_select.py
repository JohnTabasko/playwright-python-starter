from playwright.sync_api import expect, Page

from tests.utils.constants import BASE_URL


def test_select(page):
    page.goto(f'{BASE_URL}savings.html')

    deposit = page.get_by_test_id('deposit')
    period = page.get_by_test_id('period')
    result = page.get_by_test_id('result')

    deposit.fill('100')

    period.select_option('6 Months')
    expect(result).to_contain_text('After 6 Months you will earn $2.00 on your deposit')

    period.select_option(label='1 year')
    expect(result).to_contain_text('After 1 Year you will earn $5.00 on your deposit')
