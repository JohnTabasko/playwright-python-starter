import pytest, requests

@pytest.fixture(scope='session', autouse=True)
def once_per_module():
    print('Global')