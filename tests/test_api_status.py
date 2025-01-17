def test_api_status(endpoints_loader, api_client):
    status_endpoint = endpoints_loader.get_endpoint('status')
    expected_response_body = status_endpoint.get('expected_response')['body']
    expected_status_code = status_endpoint.get('expected_response')['status_code']
    response_body, status_code = api_client.send_request(method=status_endpoint.get('method'),
                                                         endpoint=status_endpoint.get('endpoint'))
    api_client.validate_response_body( expected_response_body=expected_response_body,
                                       actual_response_body=response_body)
    api_client.validate_status_code(expected_status_code=expected_status_code, actual_status_code=status_code)

