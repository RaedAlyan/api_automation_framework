"""
This module provides functionality to load and manage API endpoints from a JSON file.

@author: Raed Eleyan.
@date: 01/17/2025
@contact: raedeleyan1@gmail.com
"""
import json
from typing import Any


class EndpointsLoader:

    def __init__(self, endpoints_file_path: str ='../config/endpoints.json'):
        """
        Initializes the EndpointsLoader with the path to the endpoints JSON file.

        :param endpoints_file_path: The file path to the JSON file containing the endpoints.'
        """
        self.endpoints_file_path = endpoints_file_path
        self.endpoints = self._load_endpoints()

    def _load_endpoints(self) -> dict:
        """
        Loads the endpoints from the specified JSON file.

        :return: a dictionary containing the endpoints.
        :raises FileNotFoundError: If the endpoints file is not found at the specified path.
        """
        try:
            with open(self.endpoints_file_path) as endpoints_file:
                endpoints = json.load(endpoints_file)
            return endpoints
        except FileNotFoundError:
            raise FileNotFoundError(f'endpoints file not found at: {self.endpoints_file_path}')
        except json.JSONDecodeError:
            raise ValueError(f'Invalid JSON format in file {self.endpoints_file_path}')

    def get_endpoint(self, endpoint_name: str) -> Any:
        """
        Retrieves a specific endpoint by its name.

        :param endpoint_name: The name of the endpoint to retrieve.
        :return: The value of the requested endpoint.
        """
        endpoint = self.endpoints.get(endpoint_name)
        if endpoint is None:
            raise KeyError(f'endpoint "{endpoint_name}" not found in the endpoints json file')
        return endpoint
