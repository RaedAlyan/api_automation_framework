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
from utils.endpoints_loader import EndpointsLoader
from utils.api_client import APIClient


class TestAllProducts:
    PRODUCTS_ENDPOINT: str = 'get_all_products'
    OK_STATUS: str = 'ok'
    BAD_REQUEST_STATUS: str = 'bad_request'

    def test_get_all_products_no_parameters(self, endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint without any parameters.

        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        products_endpoint = self._get_products_endpoint(endpoints_loader)
        expected_status_code = self._get_expected_status_code(products_endpoint)
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint')
        )

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

        # Validate the response body structure
        assert isinstance(response_body, list), "Response body should be a list of products"
        for product in response_body:
            assert "id" in product, "Product should have an 'id' field"
            assert "category" in product, "Product should have a 'category' field"
            assert "name" in product, "Product should have a 'name' field"
            assert "inStock" in product, "Product should have an 'inStock' field"


    def test_get_all_products_with_category(self, endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with the 'category' parameter.

        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        products_endpoint = self._get_products_endpoint(endpoints_loader)
        expected_status_code = self._get_expected_status_code(products_endpoint)
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"category": "coffee"}
        )

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

        # Validate the response body
        assert isinstance(response_body, list), "Response body should be a list of products"
        for product in response_body:
            assert "id" in product, "Product should have an 'id' field"
            assert product["category"] == "coffee", "All products should belong to the 'coffee' category"
            assert "name" in product, "Product should have a 'name' field"
            assert "inStock" in product, "Product should have an 'inStock' field"


    def test_get_all_products_with_multiple_parameters(self, endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with multiple parameters.

        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        products_endpoint = self._get_products_endpoint(endpoints_loader)
        expected_status_code = self._get_expected_status_code(products_endpoint)
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"category": "coffee", "results": 2, "available": "true"}
        )

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

    def test_get_all_products_invalid_results(self, endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with an invalid 'results' parameter.

        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        products_endpoint = self._get_products_endpoint(endpoints_loader)
        expected_status_code = self._get_expected_status_code(products_endpoint)
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"results": -5}
        )

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

    def _get_products_endpoint(self, endpoints_loader: EndpointsLoader) -> dict:
        """
        Helper method to get the products endpoint configuration.

        :param endpoints_loader: Fixture to load endpoint configurations.
        :return: The products endpoint configuration.
        """
        return endpoints_loader.get_endpoint(self.PRODUCTS_ENDPOINT)

    @staticmethod
    def _get_expected_status_code(products_endpoint: dict, status_type: str = OK_STATUS) -> int:
        """
        Helper method to get the expected status code.

        :param products_endpoint: The products endpoint configuration.
        :param status_type: The type of status code to retrieve (e.g., "ok", "bad_request").
        :return: The expected status code.
        """
        return products_endpoint.get('status_code').get(status_type)['code']