from playwright.sync_api import Page, expect


def test_homepage_title(page: Page):
    page.goto('http://localhost:8000/')

def test_homepage_header(page: Page):
    page.goto('http://localhost:8000/web')
    header = page.locator('h4')
    expect(header).to_be_visible()
    # assert header.text_content() == 'Register to become a member'

# def test_homepage_header(page: Page):
#     page.goto('http://localhost:8000/web/')
#     # header = page.locator('h4')
#     header = 'h4[class="mb-3"]'
#     page.wait_for_selector(header, timeout=5000)
#     actual_text = page.inner_text(header)
#     expected_text = 'Register to become a member'
#     assert actual_text == expected_text

def test_homepage_copyright(page: Page):
    page.goto('http://localhost:8000/web')
    page.wait_for_timeout(3000)
    copyright_locator = page.get_by_test_id('copyright')
    expect(copyright_locator).to_contain_text('© 2025')

# def test_damian(page: Page):
#     page.goto('http://localhost:8000')
#     expected_message = '© 2025'
#     copyright_locator = page.locator('copyright')
#     page.wait_for_selector(copyright_locator, timeout=5000)
#     actual_text = page.inner_text(copyright_locator)
#     assert expected_message in actual_text

