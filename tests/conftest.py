import pytest
from utils.endpoints_loader import EndpointsLoader
from utils.api_client import APIClient


@pytest.fixture(scope='session')
def endpoints_loader():
    """
    Fixture to initialize the EndpointsLoader class.

    :return: An instance of the EndpointsLoader class.
    """
    return EndpointsLoader()

@pytest.fixture(scope='session')
def api_client(endpoints_loader):
    """
    Fixture to initialize the APIClient class.

    :return: An instance of the APIClient class.
    """
    base_url = endpoints_loader.get_endpoint('base_url')
    return APIClient(base_url)