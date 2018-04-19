import unittest
import requests
from ProductManagement import global_base
from parameterized import parameterized
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class ReleaseProductFault(unittest.TestCase):

    def setUp(self):
        self.urlnull = global_base.BaseUrl.url(self, "/products/QWED/release")
        self.urlInvalid = global_base.BaseUrl.url(self, "/products/99999999/release")
        self.urlDraftPriceNull = global_base.BaseUrl.url(self, "/products/776/release")
        self.urlDraftQuantityNull = global_base.BaseUrl.url(self, "/products/776/release")
        self.urlRelease = global_base.BaseUrl.url(self, "/products/764/release")
        self.headers = global_base.BaseUrl.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("请求不存在", 404000, "request.not.found"),
    ])
    def test_release_product_fault(self, casename, status, message):
        r = requests.patch(self.urlnull, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品id不存在", 400000, "product.invalid"),
    ])
    def test_release_product_fault(self, casename, status, message):
        r = requests.patch(self.urlInvalid, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品id草稿,价格信息包装信息为null", 400000, "price.quantity.invalid"),
    ])
    def test_release_product_draft_all_null(self, casename, status, message):
        r = requests.patch(self.urlDraftPriceNull, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

        @parameterized.expand([
            ("产品id草稿,包装信息为null", 400000, "price.quantity.invalid"),
        ])
        def test_release_product_draft_quantity_null(self, casename, status, message):
            r = requests.patch(self.urlDraftQuantuNull, headers=self.headers)
            self.result = r.json()
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品id草稿,价格信息null", 400000, "price.quantity.invalid"),
    ])
    def test_release_product_draft_price_null(self, casename, status, message):
        r = requests.patch(self.urlDraftPriceNull, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品id以上架", 400000, "product.invalid"),
    ])
    def test_release_product_release(self, casename, status, message):
        r = requests.patch(self.urlRelease, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main":
    unittest.main()