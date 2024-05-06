from kibana.base.kibana_api_client import KibanaApiClient


class SavedObjects(KibanaApiClient):

    def find(self, **params):
        method = "get"
        path = "/saved_objects/_find"
        return self.request_rest_api(path, method=method, **params).json()
