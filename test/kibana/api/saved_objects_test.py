import unittest
from kibana.api.saved_objects import SavedObjects


class SavedObjectsTest(unittest.TestCase):
    def test_find_object(self):
        saved_objects = SavedObjects()
        query_params = {
            "type": "dashboard",
            "filter": "dashboard.attributes.title:customer_dashboard"
        }
        response = saved_objects.find(params=query_params)
        print(response)
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
