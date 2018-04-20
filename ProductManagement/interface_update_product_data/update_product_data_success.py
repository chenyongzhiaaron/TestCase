import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class UpdateProductDdataSuccess(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/products/768")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("更新产品成功", "2000", "productname", "model", 14000, "hs_code", "description", 0, "success", 768, 2000,
         "productname", "model", 14000, "hs_code", "description",),
    ])
    def test_update_product_data_success(self, casename, type, name, model, color, hs_code, description, status,
                                         message, data_id, data_type, data_name, data_model, data_color,
                                         data_hs_code, data_description):
        self.payload = {"type": type, "name": name, "model": model, "color": color, "hs_code": hs_code,
                        "description": description}
        r = requests.put(self.url, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["type"], data_type)
        self.assertEqual(self.result["data"]["name"], data_name)
        self.assertEqual(self.result["data"]["model"], data_model)
        self.assertEqual(self.result["data"]["color"], data_color)
        self.assertEqual(self.result["data"]["hs_code"], data_hs_code)
        self.assertEqual(self.result["data"]["description"], data_description)


if __name__ == "__main__":
    unittest.main()
