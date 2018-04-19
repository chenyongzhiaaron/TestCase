import unittest
import requests
import os
import sys
from parameterized import parameterized
from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)



class GetProductDetailSuccess(unittest.TestCase):

    def setUp(self,):
        # param = global_base.BaseUrl()
        # self.header = param.headers()
        self.headers = global_base.Base.headers(self)

    def tearDown(self):

        print(self.result)

    @parameterized.expand([
        ("productId存在", 0, "success", 739, 0),
    ])
    def test_get_product_detail_success(self, case_name, status, message, result_data_01, result_data_02, ):

        param = global_base.Base()
        self.url = param.url("/products/739")
        r = requests.get(self.url, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], result_data_01)
        self.assertEqual(self.result["data"]["type"], result_data_02)

    @parameterized.expand([
        ("productId不存在", 400000, "product.invalid"),
    ])
    def test_get_product_detail_error(self, casename, status, message):

        self.url = global_base.Base.url(self,"/products/0")
        r = requests.get(self.url, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

if __name__ == "__main__":
    unittest.main()
