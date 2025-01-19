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
import pytest
from base_product import BaseProduct
from utils.endpoints_loader import EndpointsLoader
from utils.api_client import APIClient


class TestAllProducts(BaseProduct):
    VALID_CATEGORIES = ["coffee", "meat-seafood", "fresh-produce", "candy", "bread-bakery", "dairy", "eggs"]
    VALID_RESULTS = [1, 5, 10, 20]
    INVALID_RESULTS = [-1, -100, 100, 1500]

    def test_get_all_products_no_parameters(self, products_endpoint: dict, endpoints_loader:
    EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint without any parameters.
        
        :param products_endpoint: Fixture to get products endpoint.
        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint')
        )

        expected_status_code = self._get_expected_status_code(endpoint=products_endpoint, status_type=self.OK_STATUS)

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

        # Validate the response body structure
        assert isinstance(response_body, list), "Response body should be a list of products"
        for product in response_body:
            assert "id" in product, "Product should have an 'id' field"
            assert "category" in product, "Product should have a 'category' field"
            assert "name" in product, "Product should have a 'name' field"
            assert "inStock" in product, "Product should have an 'inStock' field"

    @pytest.mark.parametrize("category", VALID_CATEGORIES)
    def test_get_all_products_with_category(self, products_endpoint: dict, category: str,
                                            endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with the 'category' parameter.

        :param products_endpoint: Fixture to get products endpoint.
        :param category: The category of products to filter by.
        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"category": category}
        )

        expected_status_code = self._get_expected_status_code(endpoint=products_endpoint, status_type=self.OK_STATUS)

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

        # Validate the response body
        assert isinstance(response_body, list), "Response body should be a list of products"
        for product in response_body:
            assert "id" in product, "Product should have an 'id' field"
            assert product["category"] == category, f"All products should belong to the '{category}' category"
            assert "name" in product, "Product should have a 'name' field"
            assert "inStock" in product, "Product should have an 'inStock' field"

    @pytest.mark.parametrize("category", VALID_CATEGORIES)
    @pytest.mark.parametrize("results", VALID_RESULTS)
    def test_get_all_products_with_multiple_parameters(self, category: str, results: int, products_endpoint:dict,
                                                       endpoints_loader: EndpointsLoader,
                                                       api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with multiple parameters.

        :param category: The category of products to filter by.
        :param results: The number of results to return. Must be between 1 and 20.
        :param products_endpoint: Fixture to get products endpoint.
        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """

        # Validate that results is within the allowed range
        assert 1 <= results <= 20, 'Results must be between 1 and 20'
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"category": category, "results": results, "available": "true"}
        )

        expected_status_code = self._get_expected_status_code(endpoint=products_endpoint, status_type=self.OK_STATUS)

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

        # Validate the response body structure
        assert isinstance(response_body, list), "Response body should be a list of products"
        assert len(response_body) <= results, f"Response should contain at most {results} products"
        for product in response_body:
            assert "id" in product, "Product should have an 'id' field"
            assert product["category"] == category, f"All products should belong to the '{category}' category"
            assert "name" in product, "Product should have a 'name' field"
            assert product["inStock"] is True, "All products should be in stock"

    @pytest.mark.parametrize("results", INVALID_RESULTS)
    def test_get_all_products_invalid_results(self, results: int, products_endpoint: dict,
                                              endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with an invalid 'results' parameter.

        :param results: The number of results to return.
        :param products_endpoint: Fixture to get products endpoint.
        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"results": results}
        )

        expected_status_code = self._get_expected_status_code(
            endpoint=products_endpoint,
            status_type=self.BAD_REQUEST_STATUS
        )

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

    @pytest.mark.parametrize("invalid_category", ["invalid-category", "unknown", ""])
    def test_get_all_products_invalid_category(self, invalid_category: str, products_endpoint: dict,
                                               endpoints_loader: EndpointsLoader, api_client: APIClient) -> None:
        """
        Test the get_all_products endpoint with an invalid 'category' parameter.

        :param invalid_category: An invalid category value.
        :param products_endpoint: Fixture to get products endpoint.
        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        response_body, status_code = api_client.send_request(
            method=products_endpoint.get('method'),
            endpoint=products_endpoint.get('endpoint'),
            params={"category": invalid_category}
        )

        expected_status_code = self._get_expected_status_code(
            endpoint=products_endpoint,
            status_type=self.BAD_REQUEST_STATUS
        )

        # Validate the status code
        api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)
