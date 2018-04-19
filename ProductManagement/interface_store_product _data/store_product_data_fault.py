import unittest
import requests
from ProductManagement import global_base
from parameterized import parameterized
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class StoreProductData(unittest.TestCase):

    def setUp(self):
        self.url = global_base.BaseUrl.url(self, "/products")
        self.headers = global_base.BaseUrl.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("product_pramas_null", "", "", "", "", "", "", 422000, "illegal.request.data", ['required'], ['required'], ['integer'], ['required']),
    ])
    def test_store_product_data(self, case_name, type, name, model, color, hs_code, description, status, message, result_error_01, result_error_02, result_error_03, result_error_04):
        self.payload = {"type": type, "name": name, "model": model, "color": color, "hs_code": hs_code, "description": description}
        r = requests.post(self.url, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["error"]["type"], result_error_01)
        self.assertEqual(self.result["error"]["name"], result_error_02)
        self.assertEqual(self.result["error"]["color"], result_error_03)
        self.assertEqual(self.result["error"]["description"], result_error_04)

    @parameterized.expand([
        ("product_type_null", "", "-", "1", "1", "1", "1", 422000, "illegal.request.data", ['required']),
        ("product_name_null", "1", "", "1", "1", "1", "1", 422000, "illegal.request.data", ['required']),
        ("product_model_null", "1", "-", "", "1", "1", "1", 422000, "illegal.request.data", ['required']),
        ("product_color_null", "1", "-", "2", "", "1", "1", 422000, "illegal.request.data", ['integer']),

    ])
    def test_store_product_data(self, case_name, type, name, model, color, hs_code, description, status, message, result_error,):
        self.payload = {"type": type, "name": name, "model": model, "color": color, "hs_code": hs_code, "description": description}
        r = requests.post(self.url, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        if type == "":
            self.assertEqual(self.result["error"]["type"], result_error)
        elif name == "":
            self.assertEqual(self.result['error']['name'], result_error)
        elif model == "":
            self.assertEqual(self.result["error"]['model'], result_error)
        elif color == "":
            self.assertEqual(self.result["error"]['color'], result_error)

if __name__ == "__main__":
    unittest.main()