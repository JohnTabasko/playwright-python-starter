import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, timeout=3000)  # Ustaw True dla trybu bez okna
        context = browser.new_context()
        page = context.new_page()
        yield page  # Udostępniamy stronę dla testu
        browser.close()

def test_check_text_in_copyright_locator(setup_playwright):
    page = setup_playwright

    # 1. Otwórz stronę
    page.goto("http://localhost:8000/web/")  # Podmień na URL swojej aplikacji

    # 2. Lokator elementu, w którym ma być tekst
    locator = 'h4[class="mb-3"]' # CSS selektor dla elementu z id="copyright"

    # 3. Oczekiwany tekst w elemencie
    expected_text = "Register to become a member"  # Podmień na oczekiwany tekst

    # 4. Czekanie na element
    page.wait_for_selector(locator, timeout=5000)

    # 5. Pobranie tekstu z elementu
    actual_text = page.inner_text(locator)

    # 6. Asercja: czy tekst w elemencie zawiera oczekiwany tekst
    assert expected_text in actual_text, f"Oczekiwano tekstu '{expected_text}', ale znaleziono '{actual_text}'"