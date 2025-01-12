from playwright.sync_api import BrowserType

from tests.utils.constants import BASE_URL


def test_download_zip(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=1000).new_page()
    page.goto(f'{BASE_URL}savings.html')

    with page.expect_download() as download_info:
        page.get_by_role('button', name='Download Our Offer').click()

    download = download_info.value
    print(download)
    print(download.suggested_filename)

def test_download_pdf(browser_type: BrowserType):
    page = browser_type.launch().new_page()
    page.goto(f'{BASE_URL}savings.html')

    with page.expect_download() as download_info:
        page.get_by_role('button', name='Download Our Offer').click()

    download = download_info.value
    print(download)
    print(download.suggested_filename)

    assert download.suggested_filename == 'dummy.pdf'
    download.save_as('path/...', download.suggested_filename)