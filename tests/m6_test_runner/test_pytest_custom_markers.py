import sys

import pytest

# @pytest.mark.skip(reason='...')
# @pytest.mark.skipif(sys.platform == 'win32', reason='....')
@pytest.mark.smoke
def test_smoke():
    assert 2 == 2
