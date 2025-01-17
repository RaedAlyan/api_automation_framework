"""
This module contains a test for the /status endpoint of the API.

@author: Raed Eleyan.
@date: 01/17/2025
@contact: raedeleyan1@gmail.com
"""

class TestAPIStatus:
    STATUS_ENDPOINT = "status"

    def test_api_status(self, endpoints_loader, api_client):
        """
        Test the /status endpoint of the API.

        :param endpoints_loader: Fixture to load endpoint configurations.
        :param api_client: Fixture to initialize the APIClient.
        """
        # Load the status endpoint configuration
        status_endpoint = endpoints_loader.get_endpoint(self.STATUS_ENDPOINT)
        expected_response_body = status_endpoint.get('expected_response')['body']
        expected_status_code = status_endpoint.get('expected_response')['status_code']
        # Send the request to the /status endpoint
        response_body, status_code = api_client.send_request(
            method=status_endpoint.get('method'),
            endpoint=status_endpoint.get('endpoint')
        )

        # Validate the response body
        api_client.validate_response_body(
            expected_response_body=expected_response_body,
            actual_response_body=response_body
        )

        # Validate the status code
        api_client.validate_status_code(
            expected_status_code=expected_status_code,
            actual_status_code=status_code
        )
