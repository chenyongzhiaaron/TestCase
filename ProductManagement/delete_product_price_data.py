import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)


class DelectdeProductPrice(unittest.TestCase):
    def setUp(self):
        self.urlIdNull = global_base.Base.url(self, "/prices/{id}")  # 不合法 id
        self.urlIdInvalid = global_base.Base.url(self, "/prices/900")  # id 89893 不存在数据库
        self.urlIdReleased = global_base.Base.url(self, "/products/739/prices")  # id 739 已上架
        # self.urlIdDisable = global_base.Base.url(self, "/products/588/prices")  # id 588 已下架
        # self.urlIdDraft = global_base.Base.url(self, "/products/781/prices")  # id 781 草稿
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("产品ID不合法", 404000, "request.not.found"),
    ])
    def test_delete_product_price_null(self, case, status, message):
        r = requests.delete(self.urlIdNull, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


    @parameterized.expand([
        ("产品ID不存在数据库", 400000, "price.invalid")
    ])
    def test_delete_product_price_invalid(self, case, status, message):
        r = requests.delete(self.urlIdInvalid, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("产品ID已上架", 400000, "price.invalid")
    ])
    def test_delete_product_price_invalid(self, case, status, message):
        r = requests.delete(self.urlIdInvalid, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    unittest.main()


