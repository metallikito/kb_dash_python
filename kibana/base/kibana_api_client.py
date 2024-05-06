import requests


class KibanaApiClient:
    def __init__(self):
        self.apikey = "VGExVURZOEI1VW5Ub205S05DWnI6czk1MjQxN0hUb1M5elZ1TGI0cXNuUQ=="
        self.url = "http://0.0.0.0:5601/api"

    def request_rest_api(self, path, **kwargs):
        headers = self.build_headers(**kwargs)
        url = self.url + path
        return requests.request(url=url, headers=headers, **kwargs)

    def build_headers(self, **kwargs):
        headers = {
            "Authorization": f"apikey {self.apikey}",
            "kbn-xsrf": "True",
        }

        if "ndjson_file" not in kwargs:
            headers["Content-Type"] = "application/json"

        return headers
