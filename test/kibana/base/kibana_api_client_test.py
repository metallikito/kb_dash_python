import unittest
from kibana.base.kibana_api_client import KibanaApiClient


class TestKibanaApiClient(unittest.TestCase):

    def test_find_object(self):
        kibana_api_client = KibanaApiClient()
        method = "get"
        path = "/saved_objects/_find"
        params = {
            "type": "dashboard",
            "filter": "dashboard.attributes.title:customer_dashboard"
        }
        response = kibana_api_client.request_rest_api(path, method=method, params=params)
        print(response.json())
        self.assertTrue(response)
