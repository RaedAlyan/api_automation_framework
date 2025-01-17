"""
This module provides functionality to interact with an API using the APIClient class.

The APIClient class allows sending HTTP requests (GET, POST, etc.) to a specified API endpoint
and includes methods for validating the response body and status code.

@author: Raed Eleyan.
@date: 01/17/2025
@contact: raedeleyan1@gmail.com
"""
from requests import request
from requests.exceptions import RequestException

class APIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def send_request(self, method: str, endpoint: str, **kwargs) -> tuple:
        """
        Sends an HTTP request to the specified endpoint.

        :param method: The HTTP method (e.g., "GET", "POST").
        :param endpoint: The API endpoint to send the request to.
        :param kwargs: Additional arguments to pass to requests.request.
        :return: a tuple containing the response body and status code.
        """
        url = f'{self.base_url}/{endpoint}'
        try:
            response = request(method=method,url=url, **kwargs)
            return response.json(), response.status_code
        except RequestException as e:
            raise RequestException(f'Failed to send a request to API! Error: {e}')


    @staticmethod
    def validate_response_body(expected_response_body: dict, actual_response_body: dict):
        """
        Validates that the actual response body matches the expected response body.

        :param expected_response_body: The expected response body.
        :param actual_response_body: The actual response body.
        :raises AssertionError: If the actual response body does not match the expected response body.
        """
        assert expected_response_body == actual_response_body, (
            'Actual response body does not match the expected response body! '
            f'Actual response body: {actual_response_body}, '
            f'expected response body: {expected_response_body}'
        )

    @staticmethod
    def validate_status_code(expected_status_code: int, actual_status_code: int):
        """
        Validates that the actual status code matches the expected status code.

        :param expected_status_code: The expected status code.
        :param actual_status_code: The actual status code.
        :raises AssertionError: If the actual status code does not match the expected status code.
        """
        assert expected_status_code == actual_status_code, (
            'Actual status code does not match the expected status code! '
            f'Actual status code: {actual_status_code}, '
            f'expected status code: {expected_status_code}'
        )
