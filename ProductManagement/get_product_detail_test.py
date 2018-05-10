import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetProductDetailSuccess(unittest.TestCase):
    def setUp(self, ):
        # param = global_base.BaseUrl()
        # self.header = param.headers()
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("productId不存在", 400000, "product.invalid"),
    ])
    def test_get_product_detail_error(self, casename, status, message):
        self.url = global_base.Base.url(self, "/products/0")
        r = requests.get(self.url, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("productId以释放", 0, "success", 739, 0, "TestAirByCrazybabyNano", "MC7A3US/A", 7000, "HSCODES", "TestProduct",
         "1234",),
    ])
    def test_get_product_detail_success(self, case_name, status, message, data_id, data_type, data_name, data_model,
                                        data_color, hs_code, description, data_note, data_status, status_text,
                                        country_code, currency_code, price, name, color, price_text, units_text,
                                        net_weight_text, rough_weight_text, height_text, width_text, length_text):
        param = global_base.Base()
        self.url = param.url("/products/739")
        r = requests.get(self.url, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["type"], data_type)
        self.assertEqual(self.result["data"]["name"], data_name)
        self.assertEqual(self.result["data"]["name"], data_model)
        self.assertEqual(self.result["data"]["name"], data_color)
        self.assertEqual(self.result["data"]["name"], hs_code)
        self.assertEqual(self.result["data"]["name"], description)
        self.assertEqual(self.result["data"]["name"], data_note)
        self.assertEqual(self.result["data"]["name"], data_status)
        self.assertEqual(self.result["data"]["name"], status_text)
        self.assertEqual(self.result["data"]["name"], country_code)
        self.assertEqual(self.result["data"]["name"], currency_code)
        self.assertEqual(self.result["data"]["name"], price)
        self.assertEqual(self.result["data"]["name"], name)
        self.assertEqual(self.result["data"]["name"], color)
        self.assertEqual(self.result["data"]["name"], price_text)
        self.assertEqual(self.result["data"]["name"], units_text)
        self.assertEqual(self.result["data"]["name"], net_weight_text)
        self.assertEqual(self.result["data"]["name"], rough_weight_text)
        self.assertEqual(self.result["data"]["name"], height_text)
        self.assertEqual(self.result["data"]["name"], width_text)
        self.assertEqual(self.result["data"]["name"], length_text)


if __name__ == "__main__":
    unittest.main()
