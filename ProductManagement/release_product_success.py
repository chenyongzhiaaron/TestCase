import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class ReleaseProductSuccess(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/products/id/release")
        self.urlUnShelve = global_base.Base.url(self, "/products/739/release")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    # def test_release_product_success(self):
    #     ''' 产品id为草稿 '''
    #     r = requests.patch(self.url, headers=self.headers)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], 200)
    #     self.assertEqual(self.result["message"], "success")
    #     self.assertEqual(self.result["status"], 1000)
    #     self.assertEqual(self.result["id"], 7)
    #     self.assertEqual(self.result["status_text"], "released")

    @parameterized.expand([
        ("产品id已下架", 0, "success", 739, 0, 1000, "released"),
    ])
    def test_release_product_unShelve(self, casename, status, message, data_id, data_type, data_status,
                                      data_status_text):
        r = requests.patch(self.urlUnShelve, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["type"], data_type)
        self.assertEqual(self.result["data"]["status"], data_status)
        self.assertEqual(self.result["data"]["status_text"], data_status_text)


if __name__ == "__main":
    unittest.main()
