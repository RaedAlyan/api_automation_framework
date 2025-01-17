"""
This module contains tests for the /products endpoint of the API.

The tests cover various scenarios, including:
    - Fetching products without any parameters.
    - Fetching products with specific parameters (e.g., category, results, availability).
    - Handling invalid parameters and error responses.

@author: Raed Eleyan.
@date: 01/17/2025
@contact: raedeleyan1@gmail.com
"""


def test_get_all_products_no_parameters(endpoints_loader, api_client):
    """
    Test the get_all_products endpoint without any parameters.
    """
    products_endpoint = endpoints_loader.get_endpoint('get_all_products')
    expected_status_code = products_endpoint.get('status_code').get('ok')['code']
    response_body, status_code = api_client.send_request(method=products_endpoint.get('method'),
                                                         endpoint=products_endpoint.get('endpoint'))

    # Validate the status code
    api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

    # Validate the response body structure
    assert isinstance(response_body, list), "Response body should be a list of products"
    for product in response_body:
        assert "id" in product, "Product should have an 'id' field"
        assert "category" in product, "Product should have a 'category' field"
        assert "name" in product, "Product should have a 'name' field"
        assert "inStock" in product, "Product should have an 'inStock' field"


def test_get_all_products_with_category(endpoints_loader, api_client):
    """
    Test the get_all_products endpoint with the 'category' parameter.
    """
    products_endpoint = endpoints_loader.get_endpoint('get_all_products')
    expected_status_code = products_endpoint.get('status_code').get('ok')['code']
    response_body, status_code = api_client.send_request(method=products_endpoint.get('method'),
                                                         endpoint=products_endpoint.get('endpoint'),
                                                         params={"category": "coffee"})

    # Validate the status code
    api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

    # Validate the response body
    assert isinstance(response_body, list), "Response body should be a list of products"
    for product in response_body:
        assert "id" in product, "Product should have an 'id' field"
        assert product["category"] == "coffee", "All products should belong to the 'coffee' category"
        assert "name" in product, "Product should have a 'name' field"
        assert "inStock" in product, "Product should have an 'inStock' field"


def test_get_all_products_with_multiple_parameters(endpoints_loader, api_client):
    """
    Test the get_all_products endpoint with multiple parameters.
    """
    products_endpoint = endpoints_loader.get_endpoint('get_all_products')
    expected_status_code = products_endpoint.get('status_code').get('ok')['code']
    response_body, status_code = api_client.send_request(
        method=products_endpoint.get('method'),
        endpoint=products_endpoint.get('endpoint'),
        params={"category": "coffee", "results": 2, "available": "true"})

    # Validate the status code
    api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

    # Validate the response body structure
    assert isinstance(response_body, list), "Response body should be a list of products"
    assert len(response_body) <= 2, "Response should contain at most 2 products"
    for product in response_body:
        assert "id" in product, "Product should have an 'id' field"
        assert product["category"] == "coffee", "All products should belong to the 'coffee' category"
        assert "name" in product, "Product should have a 'name' field"
        assert product["inStock"] is True, "All products should be in stock"

def test_get_all_products_invalid_results(endpoints_loader, api_client):
    """
    Test the get_all_products endpoint with an invalid 'results' parameter.
    """
    products_endpoint = endpoints_loader.get_endpoint('get_all_products')
    expected_status_code = products_endpoint.get('status_code').get('bad_request')['code']
    response_body, status_code = api_client.send_request(
        method=products_endpoint.get('method'),
        endpoint=products_endpoint.get('endpoint'),
        params={"results": -5})
    api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)
