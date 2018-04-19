import unittest
import requests
from ProductManagement import global_base
from parameterized import parameterized
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class UpdateProductSuccess(unittest.TestCase):

    def setUp(self):
        self.urlAbsent = global_base.BaseUrl.url(self, "/products/abc/note")
        self.urlInvalid = global_base.BaseUrl.url(self, "/products/9999/note")
        self.headers = global_base.BaseUrl.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("请求不存在", 404000, "request.not.found"),
    ])
    def test_update_draftProduct(self, casename, status, message):
        r = requests.patch(self.urlAbsent, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品ID不存在数据库", 422000, "illegal.request.data"),
    ])
    def test_update_draftProduct(self, casename, status, message):
        r = requests.patch(self.urlInvalid, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    unittest.main()