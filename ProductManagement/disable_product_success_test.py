import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class DisableProductSuccess(unittest.TestCase):
    def setUp(self):
        self.urlRelease = global_base.Base.url(self, "/products/739/disable")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("产品id已上架", 0, "success", 739, 2000, "disabled")
    ])
    def test_disable_releaseProduct(self, casename, status, message, data_id, data_status, data_status_text):
        r = requests.patch(self.urlRelease, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["status"], data_status)
        self.assertEqual(self.result["data"]["status_text"], data_status_text)


if __name__ == "__main":
    unittest.main()
