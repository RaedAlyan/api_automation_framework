"""
This module defines pytest fixtures for loading and managing API endpoints and initializing the API client.

@author: Raed Eleyan.
@date: 01/19/2025
@contact: raedeleyan1@gmail.com
"""
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
    if base_url is None:
        raise ValueError("Base URL not found in endpoints configuration.")
    return APIClient(base_url)

@pytest.fixture(scope='session')
def products_endpoint(endpoints_loader: EndpointsLoader):
    """
    Fixture to retrieve the 'get_all_products' endpoint from the EndpointsLoader.

    :param endpoints_loader: An instance of the EndpointsLoader class.
    :return: The endpoint for getting all products.
    """
    all_product_endpoint = endpoints_loader.get_endpoint('get_all_products')
    if all_product_endpoint is None:
        raise ValueError("'get_all_products' endpoint not found in endpoints configuration.")
    return all_product_endpoint
