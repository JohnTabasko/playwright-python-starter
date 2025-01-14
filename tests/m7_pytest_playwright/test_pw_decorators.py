from datetime import timezone

import pytest
from playwright.sync_api import Page

args: dict = {'locale': 'pl_PL', 'timezone_id': 'Europe/Warsaw'} # move to reuse
class TestThing:

    @pytest.mark.skip_browser('firefox')
    def test_one(self, page: Page):
        pass

    @pytest.mark.only_browser('firefox')
    def test_two(self, page: Page):
        pass

    @pytest.mark.browser_context_args(**args)
    def test_three(self, page: Page):
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") == "Europe/Warsaw"
        assert page.evaluate("window.navigator.languages") == ["pl-PL"]

    @pytest.mark.parametrize('arg1', ['val1',
                                      'val2'])
    @pytest.mark.browser_context_args(**args)
    @pytest.mark.smoke
    def test_four(self, page: Page, arg1: str):
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") == "Europe/Warsaw"
        assert page.evaluate("window.navigator.languages") == ["pl-PL"]
