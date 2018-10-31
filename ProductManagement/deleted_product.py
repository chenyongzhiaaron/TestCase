import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)


class DeletedProduct(unittest.TestCase):
    def setUp(self):
        self.urlIdNull = global_base.Base.url(self, "/products/{id}")  # 不合法 id
        self.urlIdInvalid = global_base.Base.url(self, "/products/89893")  # id 89893 不存在数据库
        self.urlIdReleased = global_base.Base.url(self, "/products/739")  # id 739 已上架
        self.urlIdDisable = global_base.Base.url(self, "/products/716")  # id 716 已下架
        self.urlIdDraft = global_base.Base.url(self, "/products/781")  # id 782 草稿
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("ID不合法", 404000, "request.not.found"),
    ])
    def test_deleted_product_null(self, case, status, message):
        r = requests.delete(self.urlIdNull, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("ID不存在数据库", 400000, "product.invalid"),
    ])
    def test_deleted_product_invalid(self, case, status, message):
        r = requests.delete(self.urlIdInvalid, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("ID以释放", 400000, "product.invalid"),
    ])
    def test_deleted_product_released(self, case, status, message):
        r = requests.delete(self.urlIdReleased, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("id 以下架", 400000, "product.invalid"),
    ])
    def test_deleted_product_disable(self, case, status, message):
        r = requests.delete(self.urlIdDisable, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

        # @parameterized.expand([
        #     ("id 草稿", 0, "success"),
        # ])
        # def test_deleted_product_success(self, case, status, message):
        #     r = requests.delete(self.urlIdDraft, headers=self.header)
        #     self.result = r.json()
        #     self.assertEqual(self.result["status"], status)
        #     self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    unittest.main()
