import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class DisableProductFault(unittest.TestCase):
    def setUp(self):
        self.urlInvalid = global_base.Base.url(self, "/products/abc/disable")
        self.urlIdInvalid = global_base.Base.url(self, "/products/9000/disable")
        self.urlIdDisabled = global_base.Base.url(self, "/products/764/disable")
        self.urlIdDraft = global_base.Base.url(self, "/products/776/disable")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("id不存在", 404000, "request.not.found")
    ])
    def test_disable_releaseProduct(self, casename, status, message):
        r = requests.patch(self.urlInvalid, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品ID无效", 400000, "product.invalid")
    ])
    def test_disable_releaseProduct(self, casename, status, message):
        r = requests.patch(self.urlIdInvalid, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品ID草稿", 400000, "product.invalid")
    ])
    def test_disable_draftProduct(self, casename, status, message):
        r = requests.patch(self.urlIdDraft, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main":
    unittest.main()
