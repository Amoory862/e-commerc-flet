import json
import requests

class HttpHelper:
    _base_url = 'https://your-api-base-url.com'  # Replace with your API base URL

    @staticmethod
    def get(endpoint: str) -> dict:
        """Helper method to make a GET request"""
        response = requests.get(f'{HttpHelper._base_url}/{endpoint}')
        return HttpHelper._handle_response(response)

    @staticmethod
    def post(endpoint: str, data: dict) -> dict:
        """Helper method to make a POST request"""
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            f'{HttpHelper._base_url}/{endpoint}',
            headers=headers,
            data=json.dumps(data)
        )
        return HttpHelper._handle_response(response)

    @staticmethod
    def put(endpoint: str, data: dict) -> dict:
        """Helper method to make a PUT request"""
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            f'{HttpHelper._base_url}/{endpoint}',
            headers=headers,
            data=json.dumps(data)
        )
        return HttpHelper._handle_response(response)

    @staticmethod
    def delete(endpoint: str) -> dict:
        """Helper method to make a DELETE request"""
        response = requests.delete(f'{HttpHelper._base_url}/{endpoint}')
        return HttpHelper._handle_response(response)

    @staticmethod
    def _handle_response(response: requests.Response) -> dict:
        """Handle the HTTP response"""
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to load data: {response.status_code}')

# Example usage:
if __name__ == '__main__':
    try:
        # Example GET request
        data = HttpHelper.get('example-endpoint')
        print(data)

        # Example POST request
        post_data = {'key': 'value'}
        response = HttpHelper.post('example-endpoint', post_data)
        print(response)

        # Example PUT request
        put_data = {'key': 'new_value'}
        response = HttpHelper.put('example-endpoint', put_data)
        print(response)

        # Example DELETE request
        response = HttpHelper.delete('example-endpoint')
        print(response)
    except Exception as e:
        print(e)
